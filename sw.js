/* ===========================================================
 * sw.js - Upgraded
 * ===========================================================
 * Copyright 2024 @Shan
 * Licensed under Apache 2.0
 * Service Worker Script
 * ========================================================== */

// Dynamic Cache Versioning
const CACHE_VERSION = 'v2';
const CACHE_NAMESPACE = 'main-';
const CACHE_NAME = `${CACHE_NAMESPACE}${CACHE_VERSION}`;

// Precache List
const PRECACHE_LIST = [
  "./",
  "./offline.html",
  "./js/jquery.min.js",
  "./js/bootstrap.min.js",
  "./js/hux-blog.min.js",
  "./js/snackbar.js",
  "./img/icon_wechat.png",
  "./img/avatar-hux.jpg",
  "./img/home-bg.jpg",
  "./img/404-bg.jpg",
  "./css/hux-blog.min.css",
  "./css/bootstrap.min.css"
];

const HOSTNAME_WHITELIST = [
  self.location.hostname,
  "huangxuan.me",
  "yanshuo.io",
  "cdnjs.cloudflare.com"
];

const DEPRECATED_CACHES = ['precache-v1', 'runtime', 'main-precache-v1', 'main-runtime'];

// Utility Functions
const getCacheBustingUrl = (req) => {
  const url = new URL(req.url);
  url.protocol = self.location.protocol;
  url.search += (url.search ? '&' : '?') + 'cache-bust=' + Date.now();
  return url.href;
};

const isNavigationReq = (req) => req.mode === 'navigate' || (req.method === 'GET' && req.headers.get('accept').includes('text/html'));

const endWithExtension = (req) => Boolean(new URL(req.url).pathname.match(/\.\w+$/));

const shouldRedirect = (req) => isNavigationReq(req) && !new URL(req.url).pathname.endsWith("/") && !endWithExtension(req);

const getRedirectUrl = (req) => {
  const url = new URL(req.url);
  url.pathname += "/";
  return url.href;
};

// Install Event - Precache Static Assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(PRECACHE_LIST)
        .then(() => self.skipWaiting())
        .catch(err => console.error('Failed to precache:', err));
    })
  );
});

// Activate Event - Clean Up Old Caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => Promise.all(
      cacheNames
        .filter(cacheName => DEPRECATED_CACHES.includes(cacheName) || !cacheName.includes(CACHE_VERSION))
        .map(cacheName => caches.delete(cacheName))
    ))
  );
  console.log(`${CACHE_NAME} activated.`);
  event.waitUntil(self.clients.claim());
});

// Fetch Event - Handle Requests
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  if (HOSTNAME_WHITELIST.includes(url.hostname)) {

    if (shouldRedirect(event.request)) {
      event.respondWith(Response.redirect(getRedirectUrl(event.request)));
      return;
    }

    if (event.request.url.includes('ys.static')) {
      event.respondWith(cacheFirstStrategy(event.request));
      return;
    }

    event.respondWith(staleWhileRevalidateStrategy(event));
  } else {
    event.respondWith(fetch(event.request).catch(() => caches.match('offline.html')));
  }
});

// Cache-First Strategy for Static Resources
const cacheFirstStrategy = (request) => {
  return caches.match(request)
    .then(response => response || fetchAndCache(request))
    .catch(() => caches.match('offline.html'));
};

// Stale-While-Revalidate Strategy for Dynamic Content
const staleWhileRevalidateStrategy = (event) => {
  const request = event.request;
  const cache = caches.match(request);
  const fetchRequest = fetch(getCacheBustingUrl(request), { cache: "no-store" })
    .then(response => {
      if (response.ok) {
        const responseClone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
      }
      return response;
    }).catch(() => cache);

  return event.respondWith(cache || fetchRequest);
};

// Fetch and Cache Helper
const fetchAndCache = (request) => {
  return fetch(request).then(response => {
    if (response.ok) {
      const responseClone = response.clone();
      caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
    }
    return response;
  });
};

// Broadcast Message to All Clients
const sendMessageToClients = (msg) => {
  self.clients.matchAll().then(clients => {
    clients.forEach(client => client.postMessage(msg));
  });
};

// Background Sync for Failed Requests
self.addEventListener('sync', event => {
  if (event.tag === 'retry-fetch') {
    event.waitUntil(retryFailedRequests());
  }
});

const retryFailedRequests = () => {
  // Implement retry logic here for failed requests
};

