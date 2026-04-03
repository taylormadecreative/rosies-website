/* =====================================================
   ROSIE'S BEAUTY SPA — SHARED COMPONENTS
   Injects nav + footer HTML, wires up accordions
   ===================================================== */

(function () {
  'use strict';

  /* ─── Nav HTML ─────────────────────────────────────── */
  const navHTML = `
    <a href="/" class="site-nav__logo" aria-label="Rosie's Beauty Spa — Home">
      <img src="/assets/images/rosies-logo-light.jpg" alt="Rosie's Beauty Spa" width="160" height="52">
    </a>

    <nav class="site-nav__links desktop-only" aria-label="Main navigation">
      <div class="nav-dropdown-wrap">
        <a href="/services/">Services</a>
        <div class="nav-dropdown">
          <a href="/services/facials">Facials</a>
          <a href="/services/microneedling">Microneedling</a>
          <a href="/services/waxing">Waxing</a>
          <a href="/services/body-treatments">Body Treatments</a>
          <a href="/services/new-clients">New Clients</a>
          <a href="/services/packages">Packages</a>
        </div>
      </div>
      <a href="/about">About</a>
      <a href="/blog/">Blog</a>
      <a href="/contact">Contact</a>
    </nav>

    <a href="/book" class="btn-primary site-nav__book desktop-only" data-track="book">Book Now</a>

    <div class="site-nav__mobile">
      <a href="tel:8174229613" class="site-nav__call" aria-label="Call us" data-track="call">
        <i class="ph ph-phone"></i>
      </a>
      <a href="/book" class="site-nav__book-mobile" data-track="book">Book</a>
      <button class="site-nav__hamburger" aria-label="Open menu" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>

    <!-- Mobile Backdrop -->
    <div class="site-nav__mobile-backdrop" aria-hidden="true"></div>

    <!-- Mobile Menu -->
    <div class="site-nav__mobile-menu" role="dialog" aria-label="Mobile navigation">
      <a href="/">Home</a>
      <a href="/services/">Services</a>
      <div class="site-nav__mobile-menu-sub">
        <a href="/services/facials">Facials</a>
        <a href="/services/microneedling">Microneedling</a>
        <a href="/services/waxing">Waxing</a>
        <a href="/services/body-treatments">Body Treatments</a>
        <a href="/services/new-clients">New Clients</a>
        <a href="/services/packages">Packages</a>
      </div>
      <a href="/about">About</a>
      <a href="/blog/">Blog</a>
      <a href="/contact">Contact</a>
      <div class="site-nav__mobile-menu-footer">
        <a href="tel:8174229613" class="mobile-menu__phone" data-track="call">
          <i class="ph ph-phone"></i> (817) 422-9613
        </a>
        <a href="https://instagram.com/rosiesbeautyspatx" class="mobile-menu__instagram" target="_blank" rel="noopener">
          <i class="ph ph-instagram-logo"></i> @rosiesbeautyspatx
        </a>
        <a href="/book" class="btn-primary" data-track="book">Book Now</a>
      </div>
    </div>
  `;

  /* ─── Footer HTML ──────────────────────────────────── */
  const footerHTML = `
    <div class="site-footer__grid">
      <!-- Brand Column -->
      <div>
        <div class="site-footer__logo">
          <img src="/assets/images/rosies-logo.png" alt="Rosie's Beauty Spa" width="160" height="52" style="filter: brightness(1.1);">
        </div>
        <p class="site-footer__tagline">Corrective Skincare. Made for Your Melanin.</p>
      </div>

      <!-- Quick Links -->
      <div>
        <h4 class="site-footer__heading">Quick Links</h4>
        <div class="site-footer__links">
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/blog/">Blog</a>
          <a href="/contact">Contact</a>
          <a href="/book" data-track="book">Book Now</a>
        </div>
      </div>

      <!-- Services -->
      <div>
        <h4 class="site-footer__heading">Services</h4>
        <div class="site-footer__links">
          <a href="/services/facials">Facials</a>
          <a href="/services/microneedling">Microneedling</a>
          <a href="/services/waxing">Waxing</a>
          <a href="/services/body-treatments">Body Treatments</a>
          <a href="/services/new-clients">New Clients</a>
          <a href="/services/packages">Packages</a>
        </div>
      </div>

      <!-- Contact -->
      <div>
        <h4 class="site-footer__heading">Contact</h4>
        <div class="site-footer__contact-item">
          <i class="ph ph-phone"></i>
          <a href="tel:8174229613">(817) 422-9613</a>
        </div>
        <div class="site-footer__contact-item">
          <i class="ph ph-map-pin"></i>
          <span>Arlington, TX 76013</span>
        </div>
        <div class="site-footer__contact-item">
          <i class="ph ph-instagram-logo"></i>
          <a href="https://instagram.com/rosiesbeautyspatx" target="_blank" rel="noopener">@rosiesbeautyspatx</a>
        </div>
        <div class="site-footer__contact-item">
          <i class="ph ph-tiktok-logo"></i>
          <a href="https://tiktok.com/@allgoodw_awood" target="_blank" rel="noopener">@allgoodw_awood</a>
        </div>
        <div class="site-footer__social">
          <a href="https://instagram.com/rosiesbeautyspatx" target="_blank" rel="noopener" aria-label="Instagram">
            <i class="ph ph-instagram-logo"></i>
          </a>
          <a href="https://tiktok.com/@allgoodw_awood" target="_blank" rel="noopener" aria-label="TikTok">
            <i class="ph ph-tiktok-logo"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="site-footer__bottom">
      <span class="site-footer__copyright">&copy; 2026 Rosie's Beauty Spa. All rights reserved.</span>
      <div class="site-footer__legal">
        <a href="/privacy">Privacy Policy</a>
        <a href="/terms">Terms of Service</a>
      </div>
    </div>
  `;

  /* ─── Inject Components ────────────────────────────── */
  function injectComponents() {
    var navEl = document.getElementById('site-nav');
    if (navEl) {
      navEl.innerHTML = navHTML;
    }

    var footerEl = document.getElementById('site-footer');
    if (footerEl) {
      footerEl.innerHTML = footerHTML;
    }
  }

  /* ─── FAQ Accordion ────────────────────────────────── */
  function initFAQ() {
    document.addEventListener('click', function (e) {
      var question = e.target.closest('.faq__question');
      if (!question) return;

      var item = question.closest('.faq__item');
      if (!item) return;

      item.classList.toggle('faq__item--open');

      var btn = question.tagName === 'BUTTON' ? question : question.querySelector('button');
      if (btn) btn.setAttribute('aria-expanded', item.classList.contains('faq__item--open'));
    });
  }

  /* ─── Service Card Accordion ───────────────────────── */
  function initServiceCards() {
    // Add keyboard accessibility attributes to all service card headers
    document.querySelectorAll('.service-card__header').forEach(function (header) {
      header.setAttribute('tabindex', '0');
      header.setAttribute('role', 'button');
      header.setAttribute('aria-expanded', 'false');
    });

    function toggleServiceCard(header) {
      var card = header.closest('.service-card');
      if (!card) return;

      var wasOpen = card.classList.contains('service-card--open');

      // Close all sibling cards (accordion behavior)
      var container = card.parentElement;
      if (container) {
        container.querySelectorAll('.service-card--open').forEach(function (s) {
          s.classList.remove('service-card--open');
          var sibHeader = s.querySelector('.service-card__header');
          if (sibHeader) sibHeader.setAttribute('aria-expanded', 'false');
        });
      }

      // Toggle clicked card
      if (!wasOpen) {
        card.classList.add('service-card--open');
        header.setAttribute('aria-expanded', 'true');
      } else {
        header.setAttribute('aria-expanded', 'false');
      }
    }

    document.addEventListener('click', function (e) {
      var header = e.target.closest('.service-card__header');
      if (!header) return;
      toggleServiceCard(header);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var header = e.target.closest('.service-card__header');
      if (!header) return;
      e.preventDefault();
      toggleServiceCard(header);
    });
  }

  /* ─── Auto-open first service card ────────────────── */
  function autoOpenFirstCard() {
    var firstCard = document.querySelector('.service-card');
    if (firstCard) firstCard.classList.add('service-card--open');
  }

  /* ─── Init ─────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    injectComponents();
    initFAQ();
    initServiceCards();
    autoOpenFirstCard();
  });
})();
