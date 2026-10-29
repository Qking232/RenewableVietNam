/**
 * Cloudflare Worker: invest.renewablevietnam.com Reverse Proxy
 * 
 * Routes incoming traffic from invest.renewablevietnam.com to origin renewablevietnam.com/invm
 * Maintains transparent subpath routing (/quyhoach -> /invm/quyhoach)
 * Preserves query strings, handles SSL/TLS termination, and rewrites Host headers for GitHub Pages.
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const originHost = 'renewablevietnam.com';

    // Normalize target path under /invm
    let path = url.pathname;
    
    // Eliminate leading slash redundancy
    if (path.startsWith('/invm')) {
      // If user accessed invest.renewablevietnam.com/invm/..., strip extra /invm prefix
      path = path.replace(/^\/invm/, '') || '/';
    }

    // Direct mapping to origin subfolder
    const originPath = `/invm${path.endsWith('/') || path.includes('.') ? path : path + '/'}`;
    const originUrl = new URL(`https://${originHost}${originPath}${url.search}`);

    // Clone request headers and enforce Host header for GitHub Pages origin resolution
    const headers = new Headers(request.headers);
    headers.set('Host', originHost);
    headers.set('X-Forwarded-Host', url.hostname);
    headers.set('X-Forwarded-Proto', 'https');

    const originRequest = new Request(originUrl.toString(), {
      method: request.method,
      headers: headers,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : null,
      redirect: 'follow'
    });

    try {
      const response = await fetch(originRequest);

      // Clone response to adjust headers if needed
      const responseHeaders = new Headers(response.headers);
      responseHeaders.set('X-Proxy-By', 'Cloudflare-Worker-Invest');
      
      // Prevent frame embedding restrictions if necessary
      responseHeaders.delete('X-Frame-Options');

      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: responseHeaders
      });
    } catch (err) {
      return new Response(`Gateway Proxy Error: ${err.message}`, {
        status: 502,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }
  }
};
