/**
 * PSAT Practice service worker.
 * Strategy: network-first for all GETs (so fresh code/styles always win),
 * falling back to cache, with a friendly offline page for navigations.
 * Bump CACHE_VERSION to invalidate old caches after big changes.
 */
const CACHE_VERSION = 'psat-v1';
const OFFLINE_URL = '/static/offline.html';

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION).then((cache) =>
      cache.addAll([
        OFFLINE_URL,
        '/static/css/style.css',
        '/static/icons/icon-192.png',
      ])
    )
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  // Let cross-origin requests (CDNs, Desmos, fonts) pass through untouched.
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(request)
      .then((response) => {
        // Cache good same-origin responses for offline fallback.
        if (response.ok && response.type === 'basic') {
          const copy = response.clone();
          caches.open(CACHE_VERSION).then((cache) => cache.put(request, copy));
        }
        return response;
      })
      .catch(async () => {
        const cached = await caches.match(request);
        if (cached) return cached;
        if (request.mode === 'navigate') {
          return caches.match(OFFLINE_URL);
        }
        return Response.error();
      })
  );
});
