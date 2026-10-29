/**
 * Cloudflare Worker: Multi-Subdomain Edge Reverse Proxy
 * 
 * Maps subdomains to origin application directories on renewablevietnam.com:
 * - wind.renewablevietnam.com   -> /projectenergy/
 * - ind.renewablevietnam.com    -> /green/
 * - ev.renewablevietnam.com     -> /evcharging/
 * - legal.renewablevietnam.com  -> /hub/
 * - invest.renewablevietnam.com -> /invm/
 * 
 * Capabilities:
 * - Preserves subdomain in the browser address bar (URL masking & path replacement)
 * - Transparent passthrough for global shared assets (/assets/*, /data/*, /vendor/*)
 * - Normalizes subpaths and directory trailing slashes
 * - Preserves full query strings
 * - Rewrites Host headers to renewablevietnam.com for GitHub Pages origin resolution
 */

const HOST_PATH_MAP = {
  'wind.renewablevietnam.com': '/projectenergy',
  'ind.renewablevietnam.com': '/green',
  'ev.renewablevietnam.com': '/evcharging',
  'legal.renewablevietnam.com': '/hub',
  'invest.renewablevietnam.com': '/invm'
};

const SHARED_PREFIXES = ['/assets/', '/data/', '/vendor/', '/_includes/', '/_layouts/'];

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const originHost = 'renewablevietnam.com';
    const hostname = url.hostname.toLowerCase();

    const targetSubfolder = HOST_PATH_MAP[hostname];

    // Fallback: If request hostname is not mapped, pass through to originHost
    if (!targetSubfolder) {
      const originUrl = new URL(`https://${originHost}${url.pathname}${url.search}`);
      const headers = new Headers(request.headers);
      headers.set('Host', originHost);
      return fetch(new Request(originUrl, { method: request.method, headers: headers, body: request.body }));
    }

    let pathname = url.pathname;

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

    const originRequest = new Request(originUrl.toString(), {
      method: request.method,
      headers: headers,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : null,
      redirect: 'follow'
    });

    try {
      const response = await fetch(originRequest);
      const responseHeaders = new Headers(response.headers);
      responseHeaders.set('X-Proxy-By', 'Cloudflare-Worker-Subdomain-Gateway');
      responseHeaders.delete('X-Frame-Options');

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
