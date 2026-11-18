'use strict';
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-nav');
toggle?.addEventListener('click', () => {
  const expanded = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(expanded));
  toggle.setAttribute('aria-label', expanded ? toggle.dataset.closeLabel : toggle.dataset.openLabel);
  nav.classList.toggle('is-open', expanded);
});
nav?.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', toggle.dataset.openLabel);
    nav.classList.remove('is-open');
    toggle.focus();
  }
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  toggle.setAttribute('aria-expanded', 'false');
  nav.classList.remove('is-open');
}));
document.querySelectorAll('[data-language-link]').forEach(link => {
  // Hashes use language-independent ids, so an exercise remains selected.
  link.addEventListener('click', () => {
    const url = new URL(link.href);
    url.hash = window.location.hash;
    link.href = url.href;
  });
});
const search = document.querySelector('#module-search');
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
search?.addEventListener('input', () => {
  const query = normalize(search.value.trim());
  let count = 0;
  document.querySelectorAll('[data-module]').forEach(card => {
    card.hidden = !normalize(card.dataset.search).includes(query);
    if (!card.hidden) count++;
  });
  document.querySelector('#search-empty').hidden = count > 0;
  document.querySelector('#search-status').textContent = query ? `${count} ${document.body.dataset.found}` : '';
});
