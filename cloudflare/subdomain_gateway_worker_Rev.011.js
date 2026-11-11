/**
 * Cloudflare Worker: Multi-Subdomain Edge Reverse Proxy & Transition Director - Rev.011
 *
 * Maps active bookmark subdomains to origin directories on renewablevietnam.com:
 * - energy.renewablevietnam.com     -> /energy/
 * - wind.renewablevietnam.com       -> /energy/
 * - industrial.renewablevietnam.com -> /industrial/
 * - legal.renewablevietnam.com      -> /invm/
 * - project.renewablevietnam.com    -> /project/ (/dc/*, /garments/* subpaths preserved)
 *
 * Legacy alias 301 direct-to-origin (single hop, zero bounce):
 * - invest.renewablevietnam.com     -> https://renewablevietnam.com/invm/...
 * - ev.renewablevietnam.com         -> https://renewablevietnam.com/evcharging/...
 * - ind.renewablevietnam.com        -> https://renewablevietnam.com/industrial/...
 */

const HOST_PATH_MAP = {
  'energy.renewablevietnam.com': '/energy',
  'wind.renewablevietnam.com': '/energy',
  'industrial.renewablevietnam.com': '/industrial',
  'legal.renewablevietnam.com': '/invm',
  'project.renewablevietnam.com': '/project'
};

const SHARED_PREFIXES = ['/assets/built/', '/assets/', '/data/', '/vendor/', '/_includes/', '/_layouts/'];

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const originHost = 'renewablevietnam.com';
    const hostname = url.hostname.toLowerCase();

    // Direct 301 consolidation for deprecated alias subdomains
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

    // Fallback passthrough to originHost
    if (!targetSubfolder) {
      const originUrl = new URL(`https://${originHost}${url.pathname}${url.search}`);
      const headers = new Headers(request.headers);
      headers.set('Host', originHost);
      return fetch(new Request(originUrl, { method: request.method, headers: headers, body: request.body }));
    }

    let pathname = url.pathname;

    // Direct 301 for legacy path aliases
    if (pathname.startsWith('/projectenergy')) {
      const remainingPath = pathname.replace(/^\/projectenergy/, '') || '/';
      return Response.redirect(`https://${originHost}/energy${remainingPath}${url.search}`, 301);
    }

    if (pathname.startsWith('/green')) {
      const remainingPath = pathname.replace(/^\/green/, '') || '/';
      return Response.redirect(`https://${originHost}/industrial${remainingPath}${url.search}`, 301);
    }

    // Shared static assets & shell modules from origin root
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
    headers.set('X-From-Worker', 'subdomain-gateway');

    const isStaticAsset = isSharedAsset || /\.(json|gz|js|css|svg|png|jpg|jpeg|webp|woff2?|ico)(\?.*)?$/i.test(pathname);

    const fetchOptions = {
      method: request.method,
      headers: headers,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : null,
      redirect: 'follow'
    };

    if (isStaticAsset && request.method === 'GET') {
      fetchOptions.cf = {
        cacheTtl: 86400,
        cacheEverything: true
      };
    }

    const originRequest = new Request(originUrl.toString(), fetchOptions);

    try {
      const response = await fetch(originRequest);
      const responseHeaders = new Headers(response.headers);
      responseHeaders.set('X-Proxy-By', 'Cloudflare-Worker-Subdomain-Gateway');
      responseHeaders.delete('X-Frame-Options');

      if (isStaticAsset && response.status === 200) {
        responseHeaders.set('Cache-Control', 'public, max-age=86400, s-maxage=86400, stale-while-revalidate=604800');
      } else {
        responseHeaders.append('Link', '<https://renewablevietnam.com>; rel=preconnect');
      }

      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: responseHeaders
      });
    } catch (err) {
      return new Response(`Subdomain Gateway Proxy Error: ${err.message}`, {
        status: 502,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }
  }
};
