/* =====================================================
   ROSIE'S BEAUTY SPA — NAVIGATION BEHAVIOR
   Scroll detection, hamburger toggle, smooth scroll
   ===================================================== */

(function () {
  'use strict';

  var SCROLL_THRESHOLD = 80;
  var nav = null;
  var hamburger = null;
  var mobileMenu = null;
  var backdrop = null;

  /* ─── Scroll: transparent → solid ──────────────────── */
  function handleScroll() {
    if (!nav) return;

    if (window.scrollY > SCROLL_THRESHOLD) {
      nav.classList.add('site-nav--solid');
      nav.classList.remove('site-nav--transparent');
    } else {
      nav.classList.remove('site-nav--solid');
      nav.classList.add('site-nav--transparent');
    }
  }

  /* ─── Focus Trap ───────────────────────────────────── */
  function trapFocus(menuEl) {
    var focusable = menuEl.querySelectorAll('a, button, input, [tabindex]:not([tabindex="-1"])');
    if (focusable.length === 0) return;
    var first = focusable[0];
    var last = focusable[focusable.length - 1];

    first.focus();

    menuEl._trapHandler = function (e) {
      if (e.key !== 'Tab') return;
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last.focus(); }
      } else {
        if (document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    };
    menuEl.addEventListener('keydown', menuEl._trapHandler);
  }

  function releaseFocus(menuEl) {
    if (menuEl._trapHandler) {
      menuEl.removeEventListener('keydown', menuEl._trapHandler);
      delete menuEl._trapHandler;
    }
  }

  /* ─── Mobile Menu Toggle ───────────────────────────── */
  function openMenu() {
    if (!mobileMenu || !backdrop || !hamburger) return;
    mobileMenu.classList.add('site-nav__mobile-menu--open');
    backdrop.classList.add('site-nav__mobile-backdrop--visible');
    hamburger.classList.add('site-nav__hamburger--open');
    hamburger.setAttribute('aria-expanded', 'true');
    hamburger.setAttribute('aria-label', 'Close menu');
    document.body.classList.add('body--menu-open');
    trapFocus(mobileMenu);
  }

  function closeMenu() {
    if (!mobileMenu || !backdrop || !hamburger) return;
    releaseFocus(mobileMenu);
    mobileMenu.classList.remove('site-nav__mobile-menu--open');
    backdrop.classList.remove('site-nav__mobile-backdrop--visible');
    hamburger.classList.remove('site-nav__hamburger--open');
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.setAttribute('aria-label', 'Open menu');
    document.body.classList.remove('body--menu-open');
    hamburger.focus();
  }

  function toggleMenu() {
    if (mobileMenu && mobileMenu.classList.contains('site-nav__mobile-menu--open')) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  /* ─── Smooth Scroll for Anchor Links ───────────────── */
  function handleAnchorClick(e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;

    var hash = link.getAttribute('href');
    if (hash === '#') return;

    var target = document.querySelector(hash);
    if (target) {
      e.preventDefault();
      closeMenu();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  /* ─── Init ─────────────────────────────────────────── */
  function init() {
    nav = document.getElementById('site-nav');
    if (!nav) return;

    hamburger = nav.querySelector('.site-nav__hamburger');
    mobileMenu = nav.querySelector('.site-nav__mobile-menu');
    backdrop = nav.querySelector('.site-nav__mobile-backdrop');

    // Set initial nav state
    handleScroll();

    // Scroll listener (passive for perf)
    window.addEventListener('scroll', handleScroll, { passive: true });

    // Hamburger click
    if (hamburger) {
      hamburger.addEventListener('click', toggleMenu);
    }

    // Backdrop click closes menu
    if (backdrop) {
      backdrop.addEventListener('click', closeMenu);
    }

    // Mobile menu link clicks close menu
    if (mobileMenu) {
      mobileMenu.addEventListener('click', function (e) {
        if (e.target.closest('a')) {
          closeMenu();
        }
      });
    }

    // Escape key closes menu
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        closeMenu();
      }
    });

    // Smooth scroll for anchor links
    document.addEventListener('click', handleAnchorClick);
  }

  // Run after components inject (components.js runs on DOMContentLoaded too)
  // Use a slight delay to ensure nav HTML is injected first
  document.addEventListener('DOMContentLoaded', function () {
    // components.js injects synchronously on DOMContentLoaded,
    // so we use requestAnimationFrame to run after it
    requestAnimationFrame(init);
  });

  // Scroll reveal
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.reveal').forEach(function (el) {
      revealObserver.observe(el);
    });
  });
})();
