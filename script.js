/* =============================================
   ПОРТФОЛИО · JS
   Без зависимостей. Работает офлайн.
   ============================================= */

(function () {
    'use strict';

    /* --- БУРГЕР-МЕНЮ --- */
    const nav = document.querySelector('.nav');
    const burger = document.querySelector('.nav__burger');
    if (burger) {
        burger.addEventListener('click', () => nav.classList.toggle('is-open'));
        document.querySelectorAll('.nav__links a').forEach(a =>
            a.addEventListener('click', () => nav.classList.remove('is-open'))
        );
    }

    /* --- АКТИВНАЯ ССЫЛКА В НАВИГАЦИИ --- */
    const path = location.pathname.replace(/\/$/, '');
    const page = path.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav__links a').forEach(a => {
        const href = a.getAttribute('href').replace(/^\.\//, '');
        if (href === page || (page === '' && href === 'index.html')) {
            a.classList.add('is-active');
        }
    });

    /* --- РАСКРЫВАЮЩИЕСЯ ПРЕДМЕТЫ --- */
    document.querySelectorAll('.subject__header').forEach(header => {
        header.addEventListener('click', () => {
            header.parentElement.classList.toggle('is-open');
        });
    });

    /* --- ПЕРВЫЙ ПРЕДМЕТ ОТКРЫТ ПО УМОЛЧАНИЮ --- */
    const firstSubject = document.querySelector('.subject');
    if (firstSubject) firstSubject.classList.add('is-open');

    /* --- АВТОПОДСЧЁТ КОЛИЧЕСТВА ФАЙЛОВ В ПРЕДМЕТЕ --- */
    document.querySelectorAll('.subject').forEach(subject => {
        const count = subject.querySelectorAll('.file').length;
        const counter = subject.querySelector('.subject__count');
        if (counter && count > 0) {
            counter.textContent = count + (count === 1 ? ' материал' : count < 5 ? ' материала' : ' материалов');
        }
    });

    /* --- АНИМАЦИЯ ПОЯВЛЕНИЯ --- */
    const candidates = document.querySelectorAll(
        '.section-card, .subject, .about-portrait, .about-text, .diploma-cover, .diploma-info, .page-hero'
    );
    candidates.forEach(el => el.classList.add('reveal'));

    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    io.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
        candidates.forEach(el => io.observe(el));
    } else {
        candidates.forEach(el => el.classList.add('is-visible'));
    }

    /* --- ПЛАВНЫЙ СКРОЛЛ ПО ЯКОРЯМ --- */
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', e => {
            const id = link.getAttribute('href');
            if (id.length < 2) return;
            const target = document.querySelector(id);
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    /* --- KONSOLE LOG --- */
    window.addEventListener('load', () => {
        const t = (performance.now() / 1000).toFixed(2);
        console.log(`%c portfolio %c загружено за ${t}s `,
            'background:#c46a3d;color:#0a0a0a;padding:4px 8px;font-family:monospace;font-weight:bold',
            'background:#161412;color:#e8dfd0;padding:4px 8px;font-family:monospace');
    });

})();
