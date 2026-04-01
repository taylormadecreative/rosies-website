/* =====================================================
   ROSIE'S BEAUTY SPA — ANALYTICS & EVENT TRACKING
   GA4 + Facebook Pixel event delegation
   ===================================================== */

window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
gtag('js', new Date());
gtag('config', 'G-61VHFZN4YL');

document.addEventListener('click', function (e) {
  /* Book button clicks */
  var bookBtn = e.target.closest('[data-track="book"]');
  if (bookBtn) {
    var service = bookBtn.dataset.service || 'general';
    gtag('event', 'book_click', { service_name: service });
    if (typeof fbq !== 'undefined') {
      fbq('track', 'Schedule', { content_name: service });
    }
  }

  /* Call button clicks */
  var callBtn = e.target.closest('[data-track="call"]');
  if (callBtn) {
    gtag('event', 'call_click');
    if (typeof fbq !== 'undefined') {
      fbq('track', 'Contact');
    }
  }
});
