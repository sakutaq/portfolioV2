#!/usr/bin/env python3
"""
Локальный сервер для портфолио.

Запуск:
    python3 server.py            # порт 8000 (или ближайший свободный)
    python3 server.py 3000       # на указанном порту

После старта сайт автоматически откроется в браузере.
Сервер не требует подключения к интернету.
"""

import http.server
import socketserver
import sys
import webbrowser
import os
from pathlib import Path

DEFAULT_PORT = 8000


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP-обработчик с короткими логами и UTF-8 MIME-типами."""

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.js':   'application/javascript; charset=utf-8',
        '.css':  'text/css; charset=utf-8',
        '.html': 'text/html; charset=utf-8',
        '.svg':  'image/svg+xml',
        '.json': 'application/json; charset=utf-8',
        '.pdf':  'application/pdf',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.zip':  'application/zip',
        '': 'application/octet-stream',
    }

    def log_message(self, fmt, *args):
        sys.stdout.write(f"  · {self.command} {self.path} → {args[1]}\n")

    def end_headers(self):
        # Отключаем кэш — удобно при редактировании HTML
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()


def find_free_port(start_port):
    """Если порт занят — берём следующий свободный."""
    import socket
    for port in range(start_port, start_port + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('', port))
                return port
            except OSError:
                continue
    return start_port


def main():
    os.chdir(Path(__file__).parent)

    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"⚠  Не удалось распознать порт «{sys.argv[1]}». Использую {DEFAULT_PORT}.")
            port = DEFAULT_PORT

    port = find_free_port(port)
    url = f"http://localhost:{port}"

    line = "─" * 52
    print()
    print(f"  ┌{line}┐")
    print(f"  │  PORTFOLIO · локальный сервер" + " " * 21 + "│")
    print(f"  ├{line}┤")
    print(f"  │  Адрес:     {url}" + " " * (52 - 13 - len(url)) + "│")
    print(f"  │  Папка:     {Path.cwd().name}" + " " * (52 - 13 - len(Path.cwd().name)) + "│")
    print(f"  │  Остановка: Ctrl+C" + " " * 32 + "│")
    print(f"  └{line}┘")
    print()
    print("  Лог запросов:")
    print()

    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        with socketserver.TCPServer(("", port), QuietHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  ✓  Сервер остановлен.\n")
        sys.exit(0)
    except OSError as e:
        print(f"\n  ✗  Ошибка запуска: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
