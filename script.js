// ─── Config ───────────────────────────────────────────────────────────────────
// Relative URL works both locally and on Vercel
const API_ENDPOINT = '/api/quote/';

// ─── Page load ────────────────────────────────────────────────────────────────
document.body.classList.add('loaded');

// ─── Mobile menu ──────────────────────────────────────────────────────────────
const menuBtn   = document.querySelector('.menu');
const mobileNav = document.querySelector('.mobile-nav');

menuBtn?.addEventListener('click', openMobileNav);
document.querySelector('.mobile-nav-close')?.addEventListener('click', closeMobileNav);
mobileNav?.addEventListener('click', e => { if (e.target === mobileNav) closeMobileNav(); });
mobileNav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobileNav));

function openMobileNav()  { mobileNav?.classList.add('open');    document.body.style.overflow = 'hidden'; }
function closeMobileNav() { mobileNav?.classList.remove('open'); document.body.style.overflow = ''; }

// ─── Language dropdown ────────────────────────────────────────────────────────
const langBtn      = document.querySelector('.language');
const langDropdown = document.querySelector('.lang-dropdown');

langBtn?.addEventListener('click', e => { e.stopPropagation(); langDropdown?.classList.toggle('open'); });
document.addEventListener('click', () => langDropdown?.classList.remove('open'));

// ─── Product tabs ─────────────────────────────────────────────────────────────
const tabs  = document.querySelectorAll('.tab');
const cards = document.querySelectorAll('.product-card');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const filter = tab.dataset.filter;
    cards.forEach(card => {
      card.classList.toggle('hidden', filter !== 'all' && card.dataset.category !== filter);
    });
  });
});

// ─── Product → quote with pre-selection ──────────────────────────────────────
// ─── Quote form: pre-select product from URL param ────────────────────────────
const productSelect = document.querySelector('select[name="product"]');
if (productSelect) {
  const preselect = new URLSearchParams(window.location.search).get('product');
  if (preselect) {
    for (const opt of productSelect.options) {
      if (opt.text.toLowerCase().includes(preselect.toLowerCase())) { opt.selected = true; break; }
    }
  }
}

// ─── Quote form submission (Formspree) ────────────────────────────────────────
const quoteForm = document.querySelector('#quoteForm');
if (quoteForm) {
  quoteForm.addEventListener('submit', async e => {
    e.preventDefault();
    const btn  = quoteForm.querySelector('[type="submit"]');
    const note = document.querySelector('#formNote');

    btn.disabled = true;
    btn.innerHTML = '<span class="spinner"></span> Sending…';
    note.className = 'form-note';
    note.textContent = '';

    try {
      const res = await fetch(API_ENDPOINT, {
        method: 'POST',
        body:   new FormData(quoteForm),
      });
      const json = await res.json().catch(() => ({}));
      if (res.ok) {
        note.textContent = '✓ Request received — we will respond within one business day.';
        note.classList.add('success');
        quoteForm.reset();
      } else {
        note.textContent = 'Error: ' + (json.error || json.missing || res.status);
        note.classList.add('error');
      }
    } catch (err) {
      note.textContent = 'Network error: ' + err.message;
      note.classList.add('error');
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'Submit quotation request <b>↗</b>';
    }
  });
}

// ─── Intersection observer: scroll reveal ────────────────────────────────────
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('visible'); revealObs.unobserve(entry.target); }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

// ─── Sticky header ────────────────────────────────────────────────────────────
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  if (!header || document.body.classList.contains('quote-page')) return;
  const scrolled = window.scrollY > 40;
  header.style.position      = scrolled ? 'fixed' : 'absolute';
  header.style.background    = scrolled ? 'rgba(6,27,48,.97)' : 'transparent';
  header.style.backdropFilter= scrolled ? 'blur(16px)' : 'none';
  header.style.borderBottom  = scrolled ? '1px solid rgba(255,255,255,.1)' : '1px solid rgba(255,255,255,.22)';
}, { passive: true });

// ─── Hero parallax ────────────────────────────────────────────────────────────
const heroBg = document.querySelector('.hero-bg');
window.addEventListener('mousemove', e => {
  if (!heroBg || window.innerWidth < 900) return;
  const x = (e.clientX / window.innerWidth  - 0.5) * 8;
  const y = (e.clientY / window.innerHeight - 0.5) * 5;
  heroBg.style.translate = `${x}px ${y}px`;
}, { passive: true });

// ─── Counter animation for hero stats ────────────────────────────────────────
function animateCount(el, to) {
  const dur = 1800, start = performance.now();
  const step = now => {
    const t    = Math.min((now - start) / dur, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    el.textContent = String(Math.round(to * ease)).padStart(2, '0');
    if (t < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const proofObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.querySelectorAll('[data-count]').forEach(el => animateCount(el, +el.dataset.count));
    proofObs.unobserve(entry.target);
  });
}, { threshold: 0.6 });

const heroProof = document.querySelector('.hero-proof');
if (heroProof) proofObs.observe(heroProof);

// ─── Gallery lightbox ────────────────────────────────────────────────────────
const lightbox        = document.querySelector('.lightbox');
const lightboxImg     = document.querySelector('.lightbox-img');
const lightboxCaption = document.querySelector('.lightbox-caption');

document.querySelectorAll('.gallery-item').forEach(item => {
  item.addEventListener('click', () => openLightbox(item));
  item.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLightbox(item); } });
});

function openLightbox(item) {
  if (!lightbox) return;
  const img = item.querySelector('img');
  const placeholder = item.querySelector('.gallery-placeholder');
  const bg = placeholder ? getComputedStyle(placeholder).backgroundImage : '';
  const bgMatch = bg.match(/url\(["']?(.*?)["']?\)/);
  if (img) {
    lightboxImg.src = img.src;
    lightboxImg.style.display = '';
  } else if (bgMatch) {
    lightboxImg.src = bgMatch[1];
    lightboxImg.style.display = '';
  } else {
    lightboxImg.removeAttribute('src');
    lightboxImg.style.display = 'none';
  }
  lightboxCaption.textContent  = item.querySelector('figcaption')?.textContent || placeholder?.dataset.photo || '';
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  lightbox?.classList.remove('open');
  document.body.style.overflow = '';
  if (lightboxImg) lightboxImg.src = '';
}

document.querySelector('.lightbox-close')?.addEventListener('click', closeLightbox);
lightbox?.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });

// ─── Back to top ─────────────────────────────────────────────────────────────
const backToTop = document.querySelector('.back-to-top');
window.addEventListener('scroll', () => {
  backToTop?.classList.toggle('visible', window.scrollY > 600);
}, { passive: true });
backToTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

// Product detail pages: show required image slots instead of misleading stock photos.
const productDetail = document.querySelector('.product-detail');
if (productDetail) {
  const productName = productDetail.querySelector('h1')?.textContent?.trim() || 'Product';
  const detailGrid = productDetail.querySelector('.detail-grid');
  const requiredGallery = document.createElement('section');
  requiredGallery.className = 'detail-required-gallery';
  [
    `${productName} · main product photo`,
    `${productName} · 3-6 gallery photos`,
    `${productName} · packaging / export cartons`,
    `${productName} · close-up quality inspection`,
    `${productName} · processing or cold-storage condition`,
  ].forEach(label => {
    const card = document.createElement('article');
    card.className = 'detail-gallery-card';
    card.dataset.photo = label;
    requiredGallery.appendChild(card);
  });
  detailGrid?.after(requiredGallery);
}
