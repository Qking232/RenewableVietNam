/* Renewable Viet Nam Unified Sleek Header & Theme Controller - Rev.002 */
(function (window, document) {
  'use strict';

  var NAV_ITEMS = [
    { id: 'cockpit', label: 'Cockpit', href: '/' },
    { id: 'energy', label: 'Energy', href: '/energy/' },
    { id: 'industrial', label: 'Industrial', href: '/industrial/' },
    { id: 'ev', label: 'EV Tech', href: '/evcharging/' },
    { id: 'legal', label: 'Legal', href: '/invm/' },
    { id: 'project', label: 'Projects', href: '/project/' }
  ];

  var host = (window.location && window.location.hostname ? window.location.hostname : '').toLowerCase();
  var isRvnDomain = host === 'renewablevietnam.com' || (host.length > 21 && host.slice(-21) === '.renewablevietnam.com');
  var isSubdomain = isRvnDomain && host !== 'renewablevietnam.com';
  var baseOrigin = isSubdomain ? 'https://renewablevietnam.com' : '';

  function readThemeCookie() {
    try {
      var m = document.cookie.match(/(?:^|;\s*)rvn_theme=(dark|light)/);
      return m ? m[1] : null;
    } catch (e) {
      return null;
    }
  }

  function getTheme() {
    var cookieTheme = readThemeCookie();
    if (cookieTheme) return cookieTheme;
    try {
      var stored = window.localStorage.getItem('rvn_theme_v2');
      if (stored === 'dark' || stored === 'light') return stored;
    } catch (e) {}
    return 'light';
  }

  function persistTheme(theme) {
    var val = theme === 'dark' ? 'dark' : 'light';
    try {
      var attrs = '; Path=/; Max-Age=31536000; SameSite=Lax';
      if (isRvnDomain) attrs += '; Domain=.renewablevietnam.com; Secure';
      else if (window.location && window.location.protocol === 'https:') attrs += '; Secure';
      document.cookie = 'rvn_theme=' + val + attrs;
    } catch (e) {}
    try {
      window.localStorage.setItem('rvn_theme_v2', val);
      window.localStorage.setItem('rvn-theme', val);
      window.localStorage.setItem('theme', val);
    } catch (e) {}
  }

  function applyTheme(theme, persist, emitEvent) {
    var isDark = theme === 'dark';
    document.documentElement.classList.toggle('dark', isDark);
    if (persist) persistTheme(isDark ? 'dark' : 'light');
    if (emitEvent) {
      try {
        window.dispatchEvent(new CustomEvent('rvn:themechange', {
          detail: { isDark: isDark, theme: isDark ? 'dark' : 'light' }
        }));
      } catch (e) {}
    }
  }

  function toggleTheme() {
    var currentlyDark = document.documentElement.classList.contains('dark');
    var next = currentlyDark ? 'light' : 'dark';
    applyTheme(next, true, true);
    return next;
  }

  function inferActiveId() {
    if (host.indexOf('energy.') === 0 || host.indexOf('wind.') === 0) return 'energy';
    if (host.indexOf('industrial.') === 0 || host.indexOf('ind.') === 0) return 'industrial';
    if (host.indexOf('ev.') === 0) return 'ev';
    if (host.indexOf('legal.') === 0 || host.indexOf('invest.') === 0) return 'legal';
    if (host.indexOf('project.') === 0) return 'project';
    var path = (window.location && window.location.pathname ? window.location.pathname : '/').toLowerCase();
    if (path.indexOf('/energy') === 0 || path.indexOf('/projectenergy') === 0) return 'energy';
    if (path.indexOf('/industrial') === 0 || path.indexOf('/calculator') === 0) return 'industrial';
    if (path.indexOf('/evcharging') === 0) return 'ev';
    if (path.indexOf('/invm') === 0) return 'legal';
    if (path.indexOf('/project') === 0 || path.indexOf('/dc') === 0 || path.indexOf('/garments') === 0) return 'project';
    if (path === '/' || path === '/index.html' || path.indexOf('/livewire') === 0) return 'cockpit';
    return '';
  }

  function renderHeader() {
    var header = document.getElementById('rvn-header');
    if (!header) return;

    var activeId = (header.getAttribute('data-active') || inferActiveId() || '').toLowerCase();
    var html = [];
    html.push('<div class="rvn-inner">');
    html.push('<a href="' + baseOrigin + '/" class="rvn-brand" aria-label="Renewable Vietnam home">');
    html.push('<img src="/assets/images/logo.svg" alt="Renewable Viet Nam" width="28" height="28" class="rvn-logo" />');
    html.push('<span class="rvn-wordmark">RENEWABLE<span class="rvn-wordmark-ext"> VIETNAM</span></span>');
    html.push('</a>');
    html.push('<nav class="rvn-nav" aria-label="Primary Navigation">');

    for (var i = 0; i < NAV_ITEMS.length; i++) {
      var item = NAV_ITEMS[i];
      var isActive = item.id === activeId;
      var href = baseOrigin + item.href;
      html.push(
        '<a href="' + href + '" class="rvn-link' + (isActive ? ' is-active' : '') + '"' +
        (isActive ? ' aria-current="page"' : '') + '>' + item.label + '</a>'
      );
    }

    html.push('</nav>');
    html.push('<button id="themeToggleBtn" class="rvn-toggle" type="button" aria-label="Toggle color theme" title="Toggle theme">');
    html.push('<svg id="sunIcon" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" /></svg>');
    html.push('<svg id="moonIcon" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" /></svg>');
    html.push('</button>');
    html.push('</div>');

    header.innerHTML = html.join('');

    var btn = document.getElementById('themeToggleBtn');
    if (btn && !btn.getAttribute('data-rvn-bound')) {
      btn.setAttribute('data-rvn-bound', '1');
      btn.addEventListener('click', toggleTheme);
    }

    function centerActiveNav() {
      var nav = header.querySelector('.rvn-nav');
      var activeEl = nav ? nav.querySelector('.rvn-link.is-active') : null;
      if (!nav || !activeEl) return;
      if (nav.scrollWidth <= nav.clientWidth || activeEl === nav.firstElementChild) {
        nav.scrollLeft = 0;
        return;
      }
      var maxScroll = Math.max(0, nav.scrollWidth - nav.clientWidth);
      var navRect = nav.getBoundingClientRect();
      var elRect = activeEl.getBoundingClientRect();
      var leftInNav = (elRect.left - navRect.left) + nav.scrollLeft;
      var target = leftInNav - (nav.clientWidth - activeEl.offsetWidth) / 2;
      nav.scrollLeft = Math.max(0, Math.min(maxScroll, target));
    }
    centerActiveNav();
    if (window.requestAnimationFrame) {
      window.requestAnimationFrame(centerActiveNav);
    }
  }

  function injectSpeculationRules(activeId) {
    try {
      if (isSubdomain) return;
      if (!window.location || (window.location.protocol !== 'http:' && window.location.protocol !== 'https:')) return;
      if (!window.HTMLScriptElement || !HTMLScriptElement.supports || !HTMLScriptElement.supports('speculationrules')) return;
      if (document.querySelector('script[type="speculationrules"][data-rvn="1"]')) return;

      var urls = [];
      for (var i = 0; i < NAV_ITEMS.length; i++) {
        if (NAV_ITEMS[i].id !== activeId) urls.push(NAV_ITEMS[i].href);
      }
      var s = document.createElement('script');
      s.type = 'speculationrules';
      s.setAttribute('data-rvn', '1');
      s.textContent = JSON.stringify({
        prerender: [{ source: 'list', urls: urls, eagerness: 'moderate' }]
      });
      (document.head || document.documentElement).appendChild(s);
    } catch (e) {}
  }

  applyTheme(getTheme(), false, false);
  renderHeader();

  var activeHeader = document.getElementById('rvn-header');
  var currentActive = activeHeader ? (activeHeader.getAttribute('data-active') || inferActiveId()) : inferActiveId();
  injectSpeculationRules(currentActive);

  window.RVN_SHELL = {
    getTheme: getTheme,
    setTheme: function (theme) { applyTheme(theme, true, true); },
    toggleTheme: toggleTheme
  };
})(window, document);
