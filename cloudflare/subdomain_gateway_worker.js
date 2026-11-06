/**
 * Cloudflare Worker: Multi-Subdomain Edge Reverse Proxy & Migration Director
 * 
 * Maps subdomains to origin application directories on renewablevietnam.com:
 * - energy.renewablevietnam.com     -> /projectenergy/
 * - wind.renewablevietnam.com       -> /projectenergy/ (legacy alias)
 * - industrial.renewablevietnam.com -> /industrial/
 * - ev.renewablevietnam.com         -> /evcharging/
 * - invest.renewablevietnam.com     -> /invm/
 * - project.renewablevietnam.com    -> /garments/
 * 
 * Edge Redirections:
 * - ind.renewablevietnam.com        -> 301 Permanent Redirect to https://industrial.renewablevietnam.com
 */

const HOST_PATH_MAP = {
  'energy.renewablevietnam.com': '/energy',
  'wind.renewablevietnam.com': '/energy',
  'industrial.renewablevietnam.com': '/industrial',
  'legal.renewablevietnam.com': '/invm',
  'invest.renewablevietnam.com': '/invm',
  'project.renewablevietnam.com': '/project'
};

const SHARED_PREFIXES = ['/assets/', '/data/', '/vendor/', '/_includes/', '/_layouts/'];

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const originHost = 'renewablevietnam.com';
    const hostname = url.hostname.toLowerCase();

    // Edge HTTP 301 Permanent Redirect: invest. -> legal.
    if (hostname === 'invest.renewablevietnam.com') {
      const destination = `https://legal.renewablevietnam.com${url.pathname}${url.search}`;
      return Response.redirect(destination, 301);
    }

    // Edge HTTP 301 Permanent Redirect: ev. -> /evcharging
    if (hostname === 'ev.renewablevietnam.com') {
      const destination = `https://${originHost}/evcharging${url.pathname}${url.search}`;
      return Response.redirect(destination, 301);
    }

    // Edge HTTP 301 Permanent Redirect: ind. -> industrial.
    if (hostname === 'ind.renewablevietnam.com') {
      const destination = `https://industrial.renewablevietnam.com${url.pathname}${url.search}`;
      return Response.redirect(destination, 301);
    }

    const targetSubfolder = HOST_PATH_MAP[hostname];

    // Fallback: If request hostname is not mapped, pass through to originHost
    if (!targetSubfolder) {
      const originUrl = new URL(`https://${originHost}${url.pathname}${url.search}`);
      const headers = new Headers(request.headers);
      headers.set('Host', originHost);
      return fetch(new Request(originUrl, { method: request.method, headers: headers, body: request.body }));
    }

    let pathname = url.pathname;

    // Edge HTTP 301 Permanent Redirect: /green -> /industrial
        // Edge HTTP 301 Permanent Redirect: /projectenergy -> /energy
    if (pathname.startsWith('/projectenergy')) {
      const remainingPath = pathname.replace(/^\/projectenergy/, '') || '/';
      return Response.redirect(`https://energy.renewablevietnam.com${remainingPath}${url.search}`, 301);
    }

    if (pathname.startsWith('/green')) {
      const remainingPath = pathname.replace(/^\/green/, '') || '/';
      return Response.redirect(`https://industrial.renewablevietnam.com${remainingPath}${url.search}`, 301);
    }


    // Check if request is for shared static assets at origin root
    const isSharedAsset = SHARED_PREFIXES.some(prefix => pathname.startsWith(prefix));

    let originPath;
    if (isSharedAsset) {
      originPath = pathname;
    } else {
      // Strip redundant targetSubfolder if client requested it directly
      if (pathname.startsWith(targetSubfolder)) {
        pathname = pathname.substring(targetSubfolder.length) || '/';
      }

      // Format path and ensure directory trailing slash for paths without file extensions
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

    // Edge cache control for static datasets, scripts and assets
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
