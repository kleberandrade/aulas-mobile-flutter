'use strict';
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-nav');
const languagePicker = document.querySelector('.language-picker');
if (languagePicker) {
  const trigger = languagePicker.querySelector('summary');
  const syncExpanded = () => trigger.setAttribute('aria-expanded', String(languagePicker.open));
  languagePicker.addEventListener('toggle', syncExpanded);
  syncExpanded();
}
function setMenuOpen(open) {
  if (!toggle || !nav) return;
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? toggle.dataset.closeLabel : toggle.dataset.openLabel);
  nav.classList.toggle('is-open', open);
}
toggle?.addEventListener('click', () => setMenuOpen(toggle.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && languagePicker?.open) {
    languagePicker.open = false;
    languagePicker.querySelector('summary').focus();
    return;
  }
  if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') {
    setMenuOpen(false);
    toggle.focus();
  }
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenuOpen(false)));
document.addEventListener('click', event => {
  if (languagePicker?.open && !languagePicker.contains(event.target)) languagePicker.open = false;
});
document.querySelectorAll('[data-language-link]').forEach(link => {
  // Section ids are shared across languages, including labs and exercises.
  link.addEventListener('click', () => {
    const url = new URL(link.href);
    url.hash = window.location.hash;
    link.href = url.href;
    if (languagePicker) languagePicker.open = false;
  });
});
const tabs = document.querySelectorAll('.module-tabs a');
function updateSection() {
  tabs.forEach(tab => {
    if (tab.hash === window.location.hash) tab.setAttribute('aria-current', 'location');
    else tab.removeAttribute('aria-current');
  });
}
window.addEventListener('hashchange', updateSection);
updateSection();
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
