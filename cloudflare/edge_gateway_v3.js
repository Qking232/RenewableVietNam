/**
 * Cloudflare Worker: Edge Gateway Architecture v3.0 - Rev.001
 *
 * High-performance edge gateway orchestrator for RenewableVietNam:
 *  - Sub-1.0s Global TTFB & First Contentful Paint optimization
 *  - Multi-subdomain reverse proxy routing with zero-bounce 301 normalization
 *  - HTTP Cache-Control stale-while-revalidate edge caching policies
 *  - Preconnect resource hints for Google Fonts and Supabase Cloud
 *  - Edge-level security headers (nosniff, strict-origin, server-timing)
 */

const HOST_PATH_MAP = {
  'energy.renewablevietnam.com': '/energy',
  'wind.renewablevietnam.com': '/energy',
  'industrial.renewablevietnam.com': '/industrial',
  'legal.renewablevietnam.com': '/invm',
  'project.renewablevietnam.com': '/project'
};

const SHARED_PREFIXES = [
  '/assets/built/',
  '/assets/',
  '/data/',
  '/vendor/',
  '/_includes/',
  '/_layouts/'
];

export default {
  async fetch(request, env, ctx) {
    const startTime = Date.now();
    const url = new URL(request.url);
    const originHost = 'renewablevietnam.com';
    const hostname = url.hostname.toLowerCase();

    // 1. Deprecated Subdomain Canonicalization (Permanent 301)
    if (hostname === 'invest.renewablevietnam.com') {
      const sub = url.pathname.replace(/^\/invm\/?/, '/');
      return Response.redirect(`https://${originHost}/invm${sub}${url.search}`, 301);
    }
    if (hostname === 'ev.renewablevietnam.com') {
      const sub = url.pathname.replace(/^\/evcharging\/?/, '/');
      return Response.redirect(`https://${originHost}/evcharging${sub}${url.search}`, 301);
    }
    if (hostname === 'ind.renewablevietnam.com') {
      const sub = url.pathname.replace(/^\/industrial\/?/, '/');
      return Response.redirect(`https://${originHost}/industrial${sub}${url.search}`, 301);
    }

    const targetSubfolder = HOST_PATH_MAP[hostname];

    // 2. Apex and Direct Pass-through Handling
    if (!targetSubfolder) {
      const originUrl = new URL(`https://${originHost}${url.pathname}${url.search}`);
      const headers = new Headers(request.headers);
      headers.set('Host', originHost);
      headers.set('X-Edge-Gateway-Version', '3.0.0-expressive');
      return fetch(new Request(originUrl, { method: request.method, headers: headers, body: request.body }));
    }

    let pathname = url.pathname;

    // 3. Legacy Path Cleanups
    if (pathname.startsWith('/projectenergy')) {
      const remainingPath = pathname.replace(/^\/projectenergy/, '') || '/';
      return Response.redirect(`https://${originHost}/energy${remainingPath}${url.search}`, 301);
    }
    if (pathname.startsWith('/green')) {
      const remainingPath = pathname.replace(/^\/green/, '') || '/';
      return Response.redirect(`https://${originHost}/industrial${remainingPath}${url.search}`, 301);
    }

    // 4. Shared Asset Route Resolution
    const isSharedAsset = SHARED_PREFIXES.some(prefix => pathname.startsWith(prefix));
    let originPath;

    if (isSharedAsset) {
      originPath = pathname;
    } else if (hostname === 'project.renewablevietnam.com' && (pathname.startsWith('/dc') || pathname.startsWith('/garments'))) {
      originPath = pathname;
    } else {
      if (pathname.startsWith(targetSubfolder)) {
        pathname = pathname.substring(targetSubfolder.length) || '/';
      }

      const hasExtension = /\.[a-zA-Z0-9]+$/.test(pathname);
      let subpath = pathname;
      if (!hasExtension && !subpath.endsWith('/')) {
        subpath += '/';
      }

      originPath = `${targetSubfolder}${subpath.startsWith('/') ? subpath : '/' + subpath}`;
    }

    const originUrl = new URL(`https://${originHost}${originPath}${url.search}`);

    const headers = new Headers(request.headers);
    headers.set('Host', originHost);
    headers.set('X-Forwarded-Host', hostname);
    headers.set('X-Forwarded-Proto', 'https');
    headers.set('X-From-Worker', 'edge-gateway-v3');

    const isStaticAsset = isSharedAsset || /\.(json|gz|js|css|svg|png|jpg|jpeg|webp|woff2?|ico)(\?.*)?$/i.test(pathname);

    const fetchOptions = {
      method: request.method,
      headers: headers,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : null,
      redirect: 'follow'
    };

    if (request.method === 'GET') {
      fetchOptions.cf = {
        cacheTtl: isStaticAsset ? 86400 : 3600,
        cacheEverything: true
      };
    }

    const originRequest = new Request(originUrl.toString(), fetchOptions);

    try {
      const response = await fetch(originRequest);
      const responseHeaders = new Headers(response.headers);
      const duration = Date.now() - startTime;

      responseHeaders.set('X-Proxy-By', 'Cloudflare-Worker-Edge-Gateway-v3');
      responseHeaders.set('X-Edge-Gateway-Version', '3.0.0-expressive');
      responseHeaders.set('Server-Timing', `edge;dur=${duration}`);
      responseHeaders.set('X-Content-Type-Options', 'nosniff');
      responseHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');
      responseHeaders.delete('X-Frame-Options');

      if (isStaticAsset && response.status === 200) {
        responseHeaders.set('Cache-Control', 'public, max-age=86400, s-maxage=86400, stale-while-revalidate=604800');
      } else if (response.status === 200) {
        responseHeaders.set('Cache-Control', 'public, max-age=3600, s-maxage=86400, stale-while-revalidate=604800');
        responseHeaders.append('Link', '<https://fonts.googleapis.com>; rel=preconnect; crossorigin');
        responseHeaders.append('Link', '<https://nkkwegvplpozirrjcxsn.supabase.co>; rel=preconnect; crossorigin');
      }

      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: responseHeaders
      });
    } catch (err) {
      return new Response(`Edge Gateway v3 Proxy Error: ${err.message}`, {
        status: 502,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }
  }
};
