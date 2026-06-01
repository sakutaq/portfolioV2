#!/usr/bin/env python3
"""
Генератор страниц курсов.

Запуск:
    python3 generate_courses.py

Создаёт файлы course-1.html ... course-4.html на основе структуры
COURSES, описанной ниже. Чтобы добавить/убрать предмет или работу —
правьте структуру COURSES и перезапустите скрипт.
"""

from pathlib import Path

# ============================================================
# СТРУКТУРА ДАННЫХ
# ============================================================
#
# Формат:
# COURSES = {
#     номер_курса: {
#         "subtitle": "Подзаголовок страницы",
#         "subjects": [
#             {
#                 "code": "INF",                       # короткий код для номера
#                 "name": "Название предмета",
#                 "folder": "informatika",             # имя папки в files/course-N/
#                 "groups": [
#                     {
#                         "title": "Лабораторные работы",
#                         "files": [
#                             ("Лабораторная работа №1", "лаб", "pdf", "lab1.pdf"),
#                             # (название, бейдж, тип, имя файла)
#                         ],
#                     },
#                 ],
#             },
#         ],
#     },
# }
# ============================================================

COURSES = {
    1: {
        "subtitle": "Первый год обучения. Введение в специальность: основы информатики, информационные технологии, фундаментальная математика.",
        "subjects": [
            {
                "code": "INF", "name": "Информатика", "folder": "informatika",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            (f"Лабораторная работа №{i}", "Лаб", "pdf", f"lab-{i}.pdf")
                            for i in range(1, 13)
                        ],
                    },
                    {
                        "title": "Самостоятельные работы",
                        "files": [
                            (f"Самостоятельная работа №{i}", "СР", "pdf", f"sr-{i}.pdf")
                            for i in [1, 2, 3, 8]
                        ],
                    },
                ],
            },
            {
                "code": "IT", "name": "Информационные технологии (ИТ)", "folder": "it",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("Лабораторная работа №1", "Лаб", "docx", "lr-1.docx"),
                            ("Лабораторная работа №3", "Лаб", "docx", "lr-3.docx"),
                            ("Лабораторная работа №4 (ч.1)", "Лаб", "docx", "lr-4-1.docx"),
                            ("Лабораторная работа №4 (ч.2)", "Лаб", "docx", "lr-4-2.docx"),
                            ("Linux: основы", "Лаб", "pdf", "linux.pdf"),
                        ],
                    },
                    {
                        "title": "Прочие материалы",
                        "files": [
                            ("Сценарий скринкаста", "Доп", "docx", "scenario.docx"),
                            ("Список литературы", "Доп", "docx", "literatura.docx"),
                        ],
                    },
                ],
            },
            {
                "code": "ITF", "name": "ИТ в физике (ИТФ)", "folder": "itf",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            (f"Лабораторная работа №{i}", "Лаб", "docx", f"lr-{i}.docx")
                            for i in range(1, 8)
                        ],
                    },
                    {
                        "title": "Курсовая работа",
                        "files": [
                            ("Курсовая работа", "Курс", "docx", "kursovaya.docx"),
                            ("Презентация к защите", "Курс", "pptx", "kursovaya-prez.pptx"),
                        ],
                    },
                ],
            },
            {
                "code": "LATM", "name": "Линейная алгебра и теория множеств (ЛАТМ)", "folder": "latm",
                "groups": [
                    {
                        "title": "Домашние задания",
                        "files": [
                            ("ДЗ: СЛАУ", "ДЗ", "docx", "dz-slau.docx"),
                            ("ДЗ: Матрицы", "ДЗ", "docx", "dz-matritsy.docx"),
                            ("ДЗ: Определители", "ДЗ", "docx", "dz-opredeliteli.docx"),
                            ("ДЗ: Ранг матрицы", "ДЗ", "docx", "dz-rang.docx"),
                        ],
                    },
                    {
                        "title": "ВСР — Внеаудиторная самостоятельная работа",
                        "files": [
                            (f"ВСР №{i}", "ВСР", "pdf", f"vsr-{i}.pdf")
                            for i in range(1, 5)
                        ],
                    },
                    {
                        "title": "ИСР — Индивидуальная самостоятельная работа",
                        "files": [
                            ("ИСР: задание 1 (СЛАУ)", "ИСР", "pdf", "isr-1.pdf"),
                            ("ИСР: письменное ДЗ", "ИСР", "pdf", "isr-2.pdf"),
                            ("ИСР: доказательства", "ИСР", "pdf", "isr-3.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "OKA", "name": "Основы компьютерной алгебры (ОКА)", "folder": "oka",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            (f"ЛР: задание {i}.{j}", "Лаб", "pdf", f"lr-{i}-{j}.pdf")
                            for i, jmax in [(1, 4), (2, 1), (3, 3)] for j in range(1, jmax + 1)
                        ],
                    },
                    {
                        "title": "ВСР",
                        "files": [
                            ("ВСР: задание 1.1", "ВСР", "pdf", "vsr-1-1.pdf"),
                            ("ВСР: задание 2.1", "ВСР", "pdf", "vsr-2-1.pdf"),
                            ("ВСР: задание 2.2", "ВСР", "pdf", "vsr-2-2.pdf"),
                            ("ВСР: задание 3.1", "ВСР", "pdf", "vsr-3-1.pdf"),
                            ("ВСР: задание 3.2", "ВСР", "pdf", "vsr-3-2.pdf"),
                        ],
                    },
                    {
                        "title": "ИСР",
                        "files": [
                            ("ИСР: задание 1.1", "ИСР", "pdf", "isr-1-1.pdf"),
                            ("ИСР: задание 2.1", "ИСР", "pdf", "isr-2-1.pdf"),
                            ("ИСР: задание 3.1", "ИСР", "pdf", "isr-3-1.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "ENG", "name": "Иностранный язык", "folder": "english",
                "groups": [
                    {
                        "title": "Контрольные и эссе",
                        "files": [
                            ("Эссе: My future profession", "Эссе", "docx", "essay-1.docx"),
                            ("Контрольная работа №1", "КР", "docx", "kr-1.docx"),
                            ("Контрольная работа №2", "КР", "docx", "kr-2.docx"),
                            ("Презентация: About me", "Презент.", "pptx", "about-me.pptx"),
                        ],
                    },
                ],
            },
        ],
    },

    2: {
        "subtitle": "Второй год обучения. Углубление в программирование, базы данных, дискретную математику и архитектуру вычислительных систем.",
        "subjects": [
            {
                "code": "PROG", "name": "Программирование", "folder": "programming",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            (f"Лабораторная работа №{i}", "Лаб", "pdf", f"lab-{i}.pdf")
                            for i in range(1, 11)
                        ],
                    },
                    {
                        "title": "Курсовая работа",
                        "files": [
                            ("Курсовая работа: текст", "Курс", "docx", "kursovaya.docx"),
                            ("Курсовая работа: исходный код", "Курс", "zip", "kursovaya-code.zip"),
                            ("Презентация к защите", "Курс", "pptx", "kursovaya-prez.pptx"),
                        ],
                    },
                ],
            },
            {
                "code": "DB", "name": "Базы данных", "folder": "database",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: проектирование БД", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: SQL — основы", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: SQL — JOIN", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: нормализация", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: триггеры и процедуры", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: транзакции", "Лаб", "pdf", "lab-6.pdf"),
                            ("ЛР №7: индексы", "Лаб", "pdf", "lab-7.pdf"),
                        ],
                    },
                    {
                        "title": "Самостоятельные работы",
                        "files": [
                            ("СР: ER-диаграмма", "СР", "pdf", "sr-1.pdf"),
                            ("СР: запросы SQL", "СР", "pdf", "sr-2.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "DM", "name": "Дискретная математика", "folder": "discrete-math",
                "groups": [
                    {
                        "title": "Домашние задания",
                        "files": [
                            ("ДЗ: теория множеств", "ДЗ", "pdf", "dz-1.pdf"),
                            ("ДЗ: отношения и функции", "ДЗ", "pdf", "dz-2.pdf"),
                            ("ДЗ: булева алгебра", "ДЗ", "pdf", "dz-3.pdf"),
                            ("ДЗ: графы", "ДЗ", "pdf", "dz-4.pdf"),
                            ("ДЗ: комбинаторика", "ДЗ", "pdf", "dz-5.pdf"),
                        ],
                    },
                    {
                        "title": "ИСР",
                        "files": [
                            ("ИСР: задание 1", "ИСР", "pdf", "isr-1.pdf"),
                            ("ИСР: задание 2", "ИСР", "pdf", "isr-2.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "ARCH", "name": "Архитектура ЭВМ", "folder": "architecture",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: системы счисления", "Лаб", "docx", "lab-1.docx"),
                            ("ЛР №2: логические элементы", "Лаб", "docx", "lab-2.docx"),
                            ("ЛР №3: сумматоры", "Лаб", "docx", "lab-3.docx"),
                            ("ЛР №4: устройство процессора", "Лаб", "docx", "lab-4.docx"),
                            ("ЛР №5: ассемблер", "Лаб", "docx", "lab-5.docx"),
                            ("ЛР №6: память", "Лаб", "docx", "lab-6.docx"),
                        ],
                    },
                ],
            },
            {
                "code": "MA", "name": "Математический анализ", "folder": "math-analysis",
                "groups": [
                    {
                        "title": "Контрольные работы",
                        "files": [
                            ("КР №1: пределы", "КР", "pdf", "kr-1.pdf"),
                            ("КР №2: производные", "КР", "pdf", "kr-2.pdf"),
                            ("КР №3: интегралы", "КР", "pdf", "kr-3.pdf"),
                            ("КР №4: ряды", "КР", "pdf", "kr-4.pdf"),
                        ],
                    },
                    {
                        "title": "Домашние задания",
                        "files": [
                            (f"ДЗ №{i}", "ДЗ", "pdf", f"dz-{i}.pdf")
                            for i in range(1, 7)
                        ],
                    },
                ],
            },
            {
                "code": "ENG", "name": "Иностранный язык", "folder": "english",
                "groups": [
                    {
                        "title": "Контрольные и проекты",
                        "files": [
                            ("Эссе: Technology in our life", "Эссе", "docx", "essay-1.docx"),
                            ("Презентация: My research project", "Презент.", "pptx", "presentation.pptx"),
                            ("Контрольная работа", "КР", "docx", "kr-1.docx"),
                        ],
                    },
                ],
            },
        ],
    },

    3: {
        "subtitle": "Третий год обучения. Веб-разработка, операционные системы, сети, алгоритмы и теория вероятностей.",
        "subjects": [
            {
                "code": "WEB", "name": "Веб-программирование", "folder": "web",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: HTML и семантическая разметка", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: CSS и Flex/Grid", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: JavaScript — основы", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: DOM и события", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: Fetch API и AJAX", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: React — введение", "Лаб", "pdf", "lab-6.pdf"),
                            ("ЛР №7: Node.js и Express", "Лаб", "pdf", "lab-7.pdf"),
                            ("ЛР №8: REST API", "Лаб", "pdf", "lab-8.pdf"),
                        ],
                    },
                    {
                        "title": "Курсовая работа",
                        "files": [
                            ("Курсовая работа: текст", "Курс", "docx", "kursovaya.docx"),
                            ("Курсовая работа: исходный код", "Курс", "zip", "kursovaya-code.zip"),
                            ("Презентация к защите", "Курс", "pptx", "kursovaya-prez.pptx"),
                        ],
                    },
                ],
            },
            {
                "code": "OS", "name": "Операционные системы", "folder": "os",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: командная строка Linux", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: процессы и сигналы", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: потоки и синхронизация", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: межпроцессное взаимодействие", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: файловая система", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: скрипты bash", "Лаб", "pdf", "lab-6.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "NET", "name": "Сети ЭВМ и телекоммуникации", "folder": "networks",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: модель OSI и TCP/IP", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: IP-адресация и маски", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: настройка Cisco в Packet Tracer", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: маршрутизация", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: VLAN и коммутация", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: анализ трафика Wireshark", "Лаб", "pdf", "lab-6.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "ALG", "name": "Алгоритмы и структуры данных", "folder": "algorithms",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: сортировки", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: поиск и хеш-таблицы", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: списки, стеки, очереди", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: деревья поиска", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: графы и обход", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: динамическое программирование", "Лаб", "pdf", "lab-6.pdf"),
                        ],
                    },
                    {
                        "title": "ИСР",
                        "files": [
                            ("ИСР №1: анализ сложности", "ИСР", "pdf", "isr-1.pdf"),
                            ("ИСР №2: жадные алгоритмы", "ИСР", "pdf", "isr-2.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "TVMS", "name": "Теория вероятностей и матстатистика", "folder": "probability",
                "groups": [
                    {
                        "title": "Домашние задания",
                        "files": [
                            ("ДЗ №1: классическая вероятность", "ДЗ", "pdf", "dz-1.pdf"),
                            ("ДЗ №2: случайные величины", "ДЗ", "pdf", "dz-2.pdf"),
                            ("ДЗ №3: нормальное распределение", "ДЗ", "pdf", "dz-3.pdf"),
                            ("ДЗ №4: статистические оценки", "ДЗ", "pdf", "dz-4.pdf"),
                            ("ДЗ №5: проверка гипотез", "ДЗ", "pdf", "dz-5.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "MOI", "name": "Методика обучения информатике", "folder": "methodology",
                "groups": [
                    {
                        "title": "Практические занятия",
                        "files": [
                            ("Конспект урока: алгоритмы", "Конспект", "docx", "konspekt-1.docx"),
                            ("Конспект урока: переменные", "Конспект", "docx", "konspekt-2.docx"),
                            ("Конспект урока: условный оператор", "Конспект", "docx", "konspekt-3.docx"),
                            ("Технологическая карта урока", "Карта", "docx", "kar-1.docx"),
                            ("Презентация к уроку", "Презент.", "pptx", "prez-1.pptx"),
                        ],
                    },
                ],
            },
        ],
    },

    4: {
        "subtitle": "Заключительный год обучения. Машинное обучение, защита информации, мобильная разработка, методика преподавания, подготовка к защите ВКР.",
        "subjects": [
            {
                "code": "ML", "name": "Машинное обучение", "folder": "ml",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: pandas и numpy", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: линейная регрессия", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: логистическая регрессия", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: деревья решений", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: случайный лес и градиентный бустинг", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: кластеризация", "Лаб", "pdf", "lab-6.pdf"),
                            ("ЛР №7: нейронные сети", "Лаб", "pdf", "lab-7.pdf"),
                            ("ЛР №8: компьютерное зрение", "Лаб", "pdf", "lab-8.pdf"),
                        ],
                    },
                    {
                        "title": "Курсовая работа",
                        "files": [
                            ("Курсовая работа: текст", "Курс", "docx", "kursovaya.docx"),
                            ("Курсовая работа: ноутбук", "Курс", "zip", "kursovaya-notebook.zip"),
                            ("Презентация к защите", "Курс", "pptx", "kursovaya-prez.pptx"),
                        ],
                    },
                ],
            },
            {
                "code": "SEC", "name": "Защита информации", "folder": "security",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: симметричное шифрование", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: асимметричное шифрование (RSA)", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: хеш-функции", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: цифровая подпись", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: SSL/TLS и сертификаты", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: анализ уязвимостей", "Лаб", "pdf", "lab-6.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "MOB", "name": "Разработка мобильных приложений", "folder": "mobile",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: Android Studio и первое приложение", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: верстка UI", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: Activity и Fragment", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: работа с сетью", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: SQLite и Room", "Лаб", "pdf", "lab-5.pdf"),
                            ("ЛР №6: публикация в Google Play", "Лаб", "pdf", "lab-6.pdf"),
                        ],
                    },
                    {
                        "title": "Итоговый проект",
                        "files": [
                            ("Итоговое приложение: отчёт", "Проект", "docx", "project.docx"),
                            ("APK сборка", "Проект", "zip", "project-apk.zip"),
                        ],
                    },
                ],
            },
            {
                "code": "SYS", "name": "Системное программирование", "folder": "systems",
                "groups": [
                    {
                        "title": "Лабораторные работы",
                        "files": [
                            ("ЛР №1: системные вызовы", "Лаб", "pdf", "lab-1.pdf"),
                            ("ЛР №2: работа с файлами на C", "Лаб", "pdf", "lab-2.pdf"),
                            ("ЛР №3: разделяемая память", "Лаб", "pdf", "lab-3.pdf"),
                            ("ЛР №4: сокеты", "Лаб", "pdf", "lab-4.pdf"),
                            ("ЛР №5: модули ядра Linux", "Лаб", "pdf", "lab-5.pdf"),
                        ],
                    },
                ],
            },
            {
                "code": "PED", "name": "Методика преподавания информатики", "folder": "pedagogy",
                "groups": [
                    {
                        "title": "Практические работы",
                        "files": [
                            ("Конспект урока: ООП", "Конспект", "docx", "konspekt-1.docx"),
                            ("Конспект урока: алгоритмы сортировки", "Конспект", "docx", "konspekt-2.docx"),
                            ("Технологическая карта урока", "Карта", "docx", "kar-1.docx"),
                            ("Контрольно-измерительные материалы", "КИМ", "docx", "kim.docx"),
                            ("Рабочая программа дисциплины", "Программа", "docx", "rp.docx"),
                            ("Презентация для урока", "Презент.", "pptx", "prez.pptx"),
                        ],
                    },
                ],
            },
            {
                "code": "GIA", "name": "Подготовка к государственному экзамену", "folder": "exam",
                "groups": [
                    {
                        "title": "Материалы подготовки",
                        "files": [
                            ("Ответы на вопросы ГЭ", "Ответы", "pdf", "gia-answers.pdf"),
                            ("Шпаргалки по разделам", "Шпора", "pdf", "gia-cheat.pdf"),
                            ("Список вопросов к экзамену", "Вопросы", "pdf", "gia-questions.pdf"),
                        ],
                    },
                ],
            },
        ],
    },
}

# ============================================================
# ГЕНЕРАТОР HTML
# ============================================================

ICON_MAP = {
    "pdf": "PDF", "docx": "DOC", "doc": "DOC",
    "pptx": "PPT", "ppt": "PPT",
    "xlsx": "XLS", "xls": "XLS",
    "zip": "ZIP", "rar": "ZIP",
    "mp4": "MP4", "mov": "MP4",
    "txt": "TXT",
}


def file_html(name, badge, ftype, fname, course_folder, subject_folder):
    """HTML для одной карточки файла."""
    icon = ICON_MAP.get(ftype, ftype.upper())
    icon_class = f"file__icon--{ftype}" if ftype in ("pdf", "docx", "pptx", "xlsx") else ""
    href = f"files/{course_folder}/{subject_folder}/{fname}"
    return f'''                            <a href="{href}" class="file" target="_blank">
                                <span class="file__icon {icon_class}">{icon}</span>
                                <div class="file__body">
                                    <span class="file__tag">{badge}</span>
                                    <span class="file__name">{name}</span>
                                    <span class="file__action">Открыть →</span>
                                </div>
                            </a>'''


def subject_html(subject, idx, course_folder):
    """HTML для одного раздела предмета."""
    groups_html = []
    for group in subject["groups"]:
        files_html = "\n".join(
            file_html(*f, course_folder=course_folder, subject_folder=subject["folder"])
            for f in group["files"]
        )
        groups_html.append(f'''                    <div class="work-group">
                        <h3 class="work-group__title">{group["title"]}</h3>
                        <div class="files">
{files_html}
                        </div>
                    </div>''')

    return f'''        <article class="subject" id="subject-{idx}">
            <header class="subject__header">
                <div class="subject__title">
                    <span class="subject__num">{subject["code"]} · {idx:02d}</span>
                    <h2 class="subject__name">{subject["name"]}</h2>
                </div>
                <span class="subject__count"></span>
                <span class="subject__toggle">+</span>
            </header>
            <div class="subject__body">
                <div class="subject__inner">
{chr(10).join(groups_html)}
                </div>
            </div>
        </article>'''


def course_page(course_num, course_data):
    """Полный HTML страницы курса."""
    folder = f"course-{course_num}"
    subjects_html = "\n\n".join(
        subject_html(s, i + 1, folder) for i, s in enumerate(course_data["subjects"])
    )

    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course_num} курс — Портфолио</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%230a0a0a'/%3E%3Ctext x='50' y='68' font-family='Georgia,serif' font-size='60' fill='%23e8dfd0' text-anchor='middle' font-style='italic'%3EП%3C/text%3E%3C/svg%3E">
</head>
<body>

    <div class="noise" aria-hidden="true"></div>

    <nav class="nav">
        <div class="nav__inner">
            <a href="index.html" class="nav__logo">
                <span class="nav__logo-mark">П</span>
                <span class="nav__logo-text">portfolio · 2026</span>
            </a>
            <ul class="nav__links">
                <li><a href="about.html">Обо мне</a></li>
                <li><a href="practice.html">Практика</a></li>
                <li><a href="course-1.html">1 курс</a></li>
                <li><a href="course-2.html">2 курс</a></li>
                <li><a href="course-3.html">3 курс</a></li>
                <li><a href="course-4.html">4 курс</a></li>
                <li><a href="diploma.html">Диплом</a></li>
            </ul>
            <button class="nav__burger" aria-label="Меню"><span></span><span></span><span></span></button>
        </div>
    </nav>

    <div class="crumbs">
        <a href="index.html">Главная</a>
        <span class="crumbs__sep">/</span>
        <span>{course_num} курс</span>
    </div>

    <header class="page-hero">
        <span class="page-hero__num">— 0{course_num + 1} / annus academicus</span>
        <h1 class="page-hero__title">{course_num}&nbsp;<em>курс</em></h1>
        <p class="page-hero__sub">{course_data["subtitle"]}</p>
    </header>

    <main class="page-body">

{subjects_html}

    </main>

    <footer class="footer">
        <div class="footer__inner">
            <p>© 2026 · РГПУ им. А. И. Герцена · Имя&nbsp;Фамилия</p>
            <p><a href="index.html">← На главную</a></p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
'''


def main():
    out_dir = Path(__file__).parent
    for num, data in COURSES.items():
        html = course_page(num, data)
        path = out_dir / f"course-{num}.html"
        path.write_text(html, encoding="utf-8")
        files_count = sum(len(g["files"]) for s in data["subjects"] for g in s["groups"])
        print(f"  ✓ {path.name}  —  {len(data['subjects'])} предметов, {files_count} файлов")

        # Создаём папки для файлов курса
        for subject in data["subjects"]:
            (out_dir / "files" / f"course-{num}" / subject["folder"]).mkdir(parents=True, exist_ok=True)

    print(f"\n  Готово. Сгенерировано {len(COURSES)} страниц курсов.")


if __name__ == "__main__":
    main()
