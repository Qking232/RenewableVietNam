/* GridTwinVN — trực quan hoá mô hình Grid_Model_Vietnam.xiidm
   Mô hình tham chiếu tĩnh: không có trào lưu công suất, không có trạng thái vận hành. */
'use strict';

const KVC = { 500: '#22c55e', 220: '#ef4444', 110: '#3b82f6' };
const KVW = { 500: 2.4, 220: 1.5, 110: 0.85 };
const KVR = { 500: 6.5, 220: 4.4, 110: 2.6 };
const FUEL = {
  HYDRO: ['#38bdf8', 'Thuỷ điện'], THERMAL: ['#f97316', 'Nhiệt điện'],
  SOLAR: ['#facc15', 'Điện mặt trời'], WIND: ['#a78bfa', 'Điện gió'],
  OTHER: ['#94a3b8', 'Nguồn khác'],
};
const KIND = {
  substation: 'Trạm biến áp', plant_yard: 'Sân phân phối nhà máy',
  switching_station: 'Trạm cắt',
};
const TILES = {
  dark: ['https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png', '© OpenStreetMap, © CARTO'],
  light: ['https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', '© OpenStreetMap, © CARTO'],
  osm: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png', '© OpenStreetMap'],
};

const S = {
  data: null, sub: new Map(), adj: new Map(),
  map: null, tile: null, lineLayer: null, subLayer: null,
  markers: new Map(),
  kv: { 500: true, 220: true, 110: true },
  kind: { substation: true, plant_yard: true, switching_station: true },
  rg: { Bac: true, Trung: true, Nam: true },
  dashed: true, onlyGen: false, byFuel: false, showLines: true, showSusp: false,
  sldMan: null, sldMode: 'sld', selected: null,
};

const $ = (q) => document.querySelector(q);
const $$ = (q) => Array.from(document.querySelectorAll(q));
const nf = (x) => (x == null ? '—' : Number(x).toLocaleString('vi-VN'));
const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/* ══ nạp dữ liệu ═══════════════════════════════════════════ */
async function boot() {
  const d = await (await fetch('data/grid.json')).json();
  S.data = d;
  d.substations.forEach((x) => S.sub.set(x.id, x));
  d.lines.forEach((l) => {
    if (!S.adj.has(l.a)) S.adj.set(l.a, []);
    if (!S.adj.has(l.b)) S.adj.set(l.b, []);
    S.adj.get(l.a) && S.adj.get(l.a).push(l);
    S.adj.get(l.b) && S.adj.get(l.b).push(l);
  });
  S.sldMan = await fetch('sld/manifest.json').then((r) => r.json()).catch(() => ({ sld: [], nad: [] }));
  S.extra = await fetch('data/content.json').then((r) => r.json()).catch(() => null);
  S.susp = await fetch('data/suspect_lines.json').then((r) => r.json()).catch(() => []);
  S.ref = await fetch('data/ref_france.json').then((r) => r.json()).catch(() => null);

  initMap(); renderOverview(); renderFuel(); renderLegendNote();
  bindFilters(); bindSearch(); bindTabs(); renderSldList();
  renderInventory(); renderQA(); renderDoc();
  redraw();
  $('#loading').classList.add('off');
}

/* ══ bản đồ ════════════════════════════════════════════════ */
function initMap() {
  S.map = L.map('map', {
    center: [16.2, 106.6], zoom: 6, minZoom: 4, maxZoom: 15,
    preferCanvas: true, zoomControl: true, attributionControl: true,
  });
  setBasemap('dark');
  S.lineLayer = L.layerGroup().addTo(S.map);
  S.subLayer = L.layerGroup().addTo(S.map);
  S.map.on('click', (e) => { if (!e.originalEvent._gt) closeDetail(); });
  S.map.on('zoomend', rescale);

  const pts = S.data.substations.filter((x) => x.lat != null).map((x) => [x.lat, x.lon]);
  if (pts.length) S.map.fitBounds(L.latLngBounds(pts).pad(0.04), { animate: false });
}

/* bán kính nút co giãn theo mức thu phóng: ở mức toàn quốc chỉ là chấm nhỏ */
function zf() {
  const z = S.map.getZoom();
  return Math.max(0.34, Math.min(1.5, 0.34 + 0.15 * (z - 5)));
}
function rescale() {
  const k = zf();
  S.markers.forEach((m, id) => {
    const x = S.sub.get(id);
    m.setRadius(Math.max(1.1, (KVR[x.kv] || 2.4) * k));
    m.setStyle({ weight: x.kind === 'plant_yard' ? Math.max(0.7, 1.6 * k) : 0.8 * k });
  });
}

function setBasemap(k) {
  if (S.tile) { S.map.removeLayer(S.tile); S.tile = null; }
  if (k === 'none') return;
  const [url, attr] = TILES[k];
  S.tile = L.tileLayer(url, { attribution: attr, subdomains: 'abcd', maxZoom: 19 }).addTo(S.map);
  S.tile.setZIndex(0);
}

function visSub(x) {
  if (!S.kv[x.kv]) return false;
  if (!S.kind[x.kind]) return false;
  if (x.rg && !S.rg[x.rg]) return false;
  if (!S.dashed && x.dashed) return false;
  if (S.onlyGen && !x.gn) return false;
  return x.lat != null;
}
const lineVis = (l) => {
  const A = S.sub.get(l.a), B = S.sub.get(l.b);
  return (!A || !A.rg || S.rg[A.rg]) && (!B || !B.rg || S.rg[B.rg]);
};

function redraw() {
  S.lineLayer.clearLayers(); S.subLayer.clearLayers(); S.markers.clear();
  const d = S.data;

  if (S.showLines) {
    for (const kv of [110, 220, 500]) {
      if (!S.kv[kv]) continue;
      for (const l of d.lines) {
        if (l.kv !== kv || l.lat1 == null) continue;
        if (!S.dashed && l.dashed) continue;
        if (l.susp && !S.showSusp) continue;
        if (!lineVis(l)) continue;
        L.polyline([[l.lat1, l.lon1], [l.lat2, l.lon2]], {
          color: l.susp ? '#f59e0b' : KVC[kv],
          weight: l.susp ? 1.1 : KVW[kv],
          opacity: l.susp ? 0.6 : (l.dashed ? 0.55 : 0.82),
          dashArray: l.susp ? '2,6' : (l.dashed ? '5,5' : null),
          interactive: true, bubblingMouseEvents: false,
        }).bindTooltip(lineTip(l), { className: 'gt', sticky: true }).addTo(S.lineLayer);
      }
    }
  }

  let n = 0;
  const k = zf();
  for (const x of d.substations) {
    if (!visSub(x)) continue;
    n++;
    const col = S.byFuel && x.gsrc ? (FUEL[x.gsrc] || FUEL.OTHER)[0] : KVC[x.kv] || '#94a3b8';
    const m = L.circleMarker([x.lat, x.lon], {
      radius: Math.max(1.1, (KVR[x.kv] || 2.4) * k),
      color: x.kind === 'plant_yard' ? col : '#0b0f16',
      weight: x.kind === 'plant_yard' ? Math.max(0.7, 1.6 * k) : 0.8 * k,
      fillColor: x.kind === 'plant_yard' ? '#0b0f16' : col,
      fillOpacity: x.kind === 'plant_yard' ? 0.75 : 0.95,
    }).bindTooltip(subTip(x), { className: 'gt' });
    m.on('click', (e) => { e.originalEvent._gt = true; openDetail(x.id); });
    m.addTo(S.subLayer);
    S.markers.set(x.id, m);
  }
  $('#drawn-note').textContent =
    `${nf(n)} điểm nút hiển thị / ${nf(d.stats.substations)} trong mô hình`;
}

const lineTip = (l) => {
  const A = S.sub.get(l.a), B = S.sub.get(l.b);
  return `<b>${esc(A ? A.name : l.a)} — ${esc(B ? B.name : l.b)}</b><br>
    ${l.kv} kV${l.dashed ? ' · công trình 2025' : ''}<br>
    ${l.cond ? esc(l.cond) + '<br>' : ''}
    ${l.km ? l.km + ' km (suy từ điện kháng)' : ''}
    ${l.susp ? `<br><span style="color:#fbbf24">Nghi ghép sai: ${l.gkm} km đường chim bay, vượt xa mức hợp lý của cấp ${l.kv} kV</span>` : ''}`;
};
const subTip = (x) => `<b>${esc(x.name)}</b><br>${x.lv.join(' / ')} kV · ${KIND[x.kind] || x.kind}
  ${x.gn ? `<br>${x.gn} tổ máy · ${nf(x.gmw)} MW` : ''}
  ${x.place ? `<br><span style="color:#8fa0bd">${esc(x.place)}</span>` : ''}`;

/* ══ bảng chi tiết ═════════════════════════════════════════ */
function openDetail(id) {
  const x = S.sub.get(id); if (!x) return;
  S.selected = id;
  const conns = (S.adj.get(id) || []);
  const byKv = {};
  conns.forEach((l) => { byKv[l.kv] = (byKv[l.kv] || 0) + 1; });
  const bays = (x.bays || '').split(';').filter(Boolean).map((seg) => {
    const [v, codes] = seg.split(':');
    const lbl = (v === '0' || !v) ? 'chưa xác định cấp' : esc(v) + ' kV';
    return `<div style="margin-bottom:6px"><span style="color:#61728f;font-size:10px">${lbl}</span><br>${
      (codes || '').split(',').filter(Boolean).map((c) => `<span class="bay">${esc(c)}</span>`).join('')}</div>`;
  }).join('');

  const hasSld = (S.sldMan.sld || []).some((s) => s.sub === id);
  const row = (a, b) => `<div class="d-row"><span>${a}</span><span>${b}</span></div>`;

  $('#detail-body').innerHTML = `
    <div class="d-title">${esc(x.name)}</div>
    <div class="d-sub">${esc(x.place || 'chưa có mô tả vị trí')}</div>
    <div class="d-tags">
      ${x.lv.map((v) => `<span class="pill p${v}">${v} kV</span>`).join('')}
      <span class="pill" style="background:#1c2739;color:#9fb3d0">${KIND[x.kind] || x.kind}</span>
      ${x.dashed ? '<span class="pill" style="background:rgba(245,158,11,.15);color:#fbbf24">công trình 2025</span>' : ''}
    </div>

    <div class="d-sec"><h3>Thiết bị trong trạm</h3>
      ${row('Thanh cái', nf(x.bb))}
      ${row('Máy cắt và dao cách ly', nf(x.sw))}
      ${row('Máy biến áp', x.tn ? `${x.tn} máy · ${nf(x.tmva)} MVA` : '—')}
      ${row('Thiết bị bù', nf(x.sh))}
      ${row('Tổ máy phát', x.gn ? `${x.gn} tổ · ${nf(x.gmw)} MW` : '—')}
      ${x.gsrc ? row('Loại nguồn', (FUEL[x.gsrc] || ['', x.gsrc])[1]) : ''}
    </div>

    <div class="d-sec"><h3>Đấu nối</h3>
      ${Object.keys(byKv).sort((a, b) => b - a).map((v) =>
    row(`Mạch ${v} kV`, byKv[v])).join('') || '<p class="note">Không có mạch nào đấu nối trong mô hình.</p>'}
    </div>

    ${bays ? `<div class="d-sec"><h3>Mã ngăn đọc từ bản vẽ</h3>${bays}</div>` : ''}

    <div class="d-sec"><h3>Nguồn gốc toạ độ</h3>
      ${row('Độ tin cậy', x.conf === 'high' ? '<span class="tag t-ok">cao</span>'
    : x.conf === 'low' ? '<span class="tag t-bad">thấp</span>' : '<span class="tag t-warn">vừa</span>')}
      ${row('Nguồn', `<span style="font-size:11px">${esc(x.gsrc_txt || '—')}</span>`)}
      ${row('Toạ độ', `${x.lat}, ${x.lon}`)}
      ${x.jit ? `<p class="note">Điểm này dùng chung một toạ độ tra cứu với ${x.jit - 1} trạm khác,
        đã được xếp lệch khoảng 700 m để không che nhau trên bản đồ.</p>` : ''}
    </div>

    <div class="d-btns">
      <button class="btn" ${hasSld ? '' : 'disabled'} onclick="gotoSld('${id}')">Sơ đồ một sợi</button>
      <button class="btn" onclick="zoomTo('${id}')">Phóng tới</button>
    </div>

    <div class="d-sec"><h3>Các mạch đấu nối</h3>
      ${conns.slice(0, 24).map((l) => {
      const o = l.a === id ? l.b : l.a; const O = S.sub.get(o);
      return `<div class="d-row"><span class="lnk" onclick="openDetail('${o}')">${esc(O ? O.name : o)}</span>
        <span><span class="pill p${l.kv}">${l.kv}</span> ${l.km ? l.km + ' km' : ''}</span></div>`;
    }).join('')}
      ${conns.length > 24 ? `<p class="note">và ${conns.length - 24} mạch khác</p>` : ''}
    </div>`;
  $('#detail').classList.remove('hidden');
}
function closeDetail() { $('#detail').classList.add('hidden'); S.selected = null; }
window.openDetail = openDetail;
window.zoomTo = (id) => { const x = S.sub.get(id); if (x && x.lat != null) S.map.setView([x.lat, x.lon], 12); };
window.gotoSld = (id) => { switchTab('sld'); pickSld(id); };

/* ══ panel trái ════════════════════════════════════════════ */
function renderOverview() {
  const s = S.data.stats;
  const items = [
    [nf(s.substations), 'điểm nút'], [nf(s.lines), 'mạch đường dây'],
    [nf(s.switches), 'thiết bị đóng cắt'], [nf(s.transformers), 'máy biến áp'],
    [nf(s.generators), 'tổ máy'], [nf(s.gen_mw) + ' MW', 'công suất đặt'],
    [nf(s.shunts), 'thiết bị bù'], [nf(s.busbars), 'thanh cái'],
  ];
  $('#overview').innerHTML = items.map(([n, l]) =>
    `<div class="kv-item"><div class="n">${n}</div><div class="l">${l}</div></div>`).join('');
  $('#src-note').textContent = `${S.data.source}. ${S.data.nature}`;
}

function renderFuel() {
  const f = S.data.stats.fuel;
  const max = Math.max(...Object.values(f).map((x) => x.mw));
  $('#fuel').innerHTML = Object.entries(f).sort((a, b) => b[1].mw - a[1].mw).map(([k, v]) =>
    `<div class="fuel-row">
      <span class="nm">${(FUEL[k] || ['', k])[1]}</span>
      <span class="fuel-bar"><i class="f-${k}" style="width:${Math.max(2, 100 * v.mw / max)}%"></i></span>
      <span class="mw">${nf(v.mw)}</span>
    </div>`).join('') +
    `<p class="note">Tổng ${nf(S.data.stats.gen_mw)} MW trên ${nf(S.data.stats.generators)} tổ máy.
     Công suất lấy theo giá trị ghi trên bản vẽ, là công suất lắp đặt chứ không phải công suất phát.</p>`;
}

function renderLegendNote() {
  const s = S.data.stats;
  $('#drawn-note').textContent = `${nf(s.geolocated)} / ${nf(s.substations)} điểm nút có toạ độ`;
}

/* ══ bộ lọc ════════════════════════════════════════════════ */
function bindFilters() {
  $$('[data-kv]').forEach((el) => el.addEventListener('change', () => {
    S.kv[el.dataset.kv] = el.checked; redraw();
  }));
  $$('[data-kind]').forEach((el) => el.addEventListener('change', () => {
    S.kind[el.dataset.kind] = el.checked; redraw();
  }));
  $$('[data-rg]').forEach((el) => el.addEventListener('change', () => {
    S.rg[el.dataset.rg] = el.checked; redraw();
  }));
  const bind = (id, key) => $(id).addEventListener('change', (e) => { S[key] = e.target.checked; redraw(); });
  bind('#f-dashed', 'dashed'); bind('#f-gen', 'onlyGen');
  bind('#f-fuel', 'byFuel'); bind('#f-lines', 'showLines'); bind('#f-susp', 'showSusp');
  $('#basemap').addEventListener('change', (e) => setBasemap(e.target.value));
  $('#reset').addEventListener('click', () => {
    $$('#left input[type=checkbox]').forEach((el) => {
      el.checked = !['f-gen', 'f-fuel', 'f-susp'].includes(el.id);
    });
    S.kv = { 500: true, 220: true, 110: true };
    S.kind = { substation: true, plant_yard: true, switching_station: true };
    S.rg = { Bac: true, Trung: true, Nam: true };
    S.dashed = true; S.onlyGen = false; S.byFuel = false; S.showLines = true; S.showSusp = false;
    redraw();
    const pts = S.data.substations.filter((x) => x.lat != null).map((x) => [x.lat, x.lon]);
    if (pts.length) S.map.fitBounds(L.latLngBounds(pts).pad(0.04));
  });
  $('#left-toggle').addEventListener('click', () => {
    const l = $('#left'); l.classList.toggle('hide');
    $('#left-toggle').textContent = l.classList.contains('hide') ? '›' : '‹';
    setTimeout(() => S.map.invalidateSize(), 220);
  });
  $('#detail-close').addEventListener('click', closeDetail);
}

/* ══ tìm kiếm ══════════════════════════════════════════════ */
const norm = (s) => String(s).normalize('NFD').replace(/[̀-ͯ]/g, '')
  .replace(/đ/g, 'd').replace(/Đ/g, 'D').toUpperCase();

function bindSearch() {
  const inp = $('#search'), box = $('#results');
  const run = () => {
    const q = norm(inp.value.trim());
    if (q.length < 2) { box.classList.remove('on'); return; }
    const hits = S.data.substations
      .filter((x) => norm(x.name).includes(q) || norm(x.place).includes(q))
      .sort((a, b) => b.kv - a.kv || a.name.length - b.name.length).slice(0, 40);
    box.innerHTML = hits.length ? hits.map((x) =>
      `<div class="res" data-id="${x.id}">
        <span class="pill p${x.kv}">${x.kv}</span>
        <div><b>${esc(x.name)}</b><small>${esc(x.place || KIND[x.kind])}${x.lat == null ? ' · chưa có toạ độ' : ''}</small></div>
      </div>`).join('') : '<div class="res"><small>Không tìm thấy</small></div>';
    box.classList.add('on');
  };
  inp.addEventListener('input', run);
  inp.addEventListener('focus', run);
  box.addEventListener('click', (e) => {
    const r = e.target.closest('.res'); if (!r || !r.dataset.id) return;
    const x = S.sub.get(r.dataset.id);
    box.classList.remove('on'); inp.value = '';
    if (x.lat != null) { switchTab('map'); S.map.setView([x.lat, x.lon], 11); }
    openDetail(x.id);
  });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('#search-wrap')) box.classList.remove('on');
  });
}

/* ══ tab ═══════════════════════════════════════════════════ */
function bindTabs() { $$('.tab').forEach((t) => t.addEventListener('click', () => switchTab(t.dataset.tab))); }
function switchTab(id) {
  $$('.tab').forEach((t) => t.classList.toggle('on', t.dataset.tab === id));
  $$('.view').forEach((v) => v.classList.toggle('on', v.id === 'view-' + id));
  if (id === 'map') setTimeout(() => S.map.invalidateSize(), 60);
}

/* ══ thư viện sơ đồ ════════════════════════════════════════ */
function renderSldList() {
  $$('#sld-kind button').forEach((b) => b.addEventListener('click', () => {
    $$('#sld-kind button').forEach((x) => x.classList.toggle('on', x === b));
    S.sldMode = b.dataset.d; fillSldItems();
  }));
  $('#sld-search').addEventListener('input', fillSldItems);
  fillSldItems();
}

function fillSldItems() {
  const q = norm($('#sld-search').value.trim());
  const list = (S.sldMan[S.sldMode] || []).filter((s) => !q || norm(s.title).includes(q));
  $('#sld-items').innerHTML = list.length ? list.map((s) =>
    `<div class="sitem" data-f="${esc(s.file)}" data-t="${esc(s.title)}" data-sub="${esc(s.sub || '')}">
      <span class="pill p${s.kv || 110}">${s.kv || ''}</span>
      <div><b>${esc(s.title)}</b><small>${esc(s.note || '')}</small></div>
    </div>`).join('')
    : '<p class="note">Chưa có sơ đồ nào khớp.</p>';
  $$('#sld-items .sitem').forEach((el) => el.addEventListener('click', () => showDiagram(el)));
}

function pickSld(subId) {
  const el = $$('#sld-items .sitem').find((e) => e.dataset.sub === subId);
  if (el) showDiagram(el); else $('#sld-search').value = '';
}

async function showDiagram(el) {
  $$('#sld-items .sitem').forEach((x) => x.classList.toggle('on', x === el));
  const f = el.dataset.f, t = el.dataset.t, sub = el.dataset.sub;
  S.zoom = 1;
  $('#sld-head').innerHTML = `
    <div style="display:flex;align-items:center;gap:14px">
      <div style="flex:1">
        <h2>${esc(t)}</h2>
        <p>${S.sldMode === 'sld' ? 'Sơ đồ một sợi dựng bằng PowSyBl từ topology node-breaker'
      : 'Sơ đồ vùng lưới (Network Area Diagram), bán kính 2 nút'} · mô hình tĩnh nên không có trạng thái đóng cắt thực tế</p>
      </div>
      <div class="seg" style="width:250px;margin:0">
        <button onclick="sldZoom(-1)">−</button>
        <button onclick="sldZoom(0)">Vừa khung</button>
        <button onclick="sldZoom(1)">+</button>
        <button onclick="window.open('${esc(f)}','_blank')">Mở SVG</button>
      </div>
      ${sub ? `<button class="btn" style="flex:none;width:112px" onclick="switchTab('map');zoomTo('${esc(sub)}');openDetail('${esc(sub)}')">Xem trên bản đồ</button>` : ''}
    </div>`;
  $('#sld-view').innerHTML = '<p class="empty">Đang dựng sơ đồ...</p>';
  try {
    const svg = await (await fetch(f)).text();
    $('#sld-view').innerHTML = svg;
    const el2 = $('#sld-view svg');
    if (el2) {
      const w = el2.getAttribute('width'), h = el2.getAttribute('height');
      if (!el2.getAttribute('viewBox') && w && h) {
        el2.setAttribute('viewBox', `0 0 ${parseFloat(w)} ${parseFloat(h)}`);
      }
      el2.removeAttribute('width'); el2.removeAttribute('height');
      el2.style.width = '100%'; el2.style.height = 'auto';
    }
  } catch (e) {
    $('#sld-view').innerHTML = '<p class="empty">Không đọc được file sơ đồ.</p>';
  }
}
window.sldZoom = (d) => {
  S.zoom = d === 0 ? 1 : Math.max(0.35, Math.min(6, (S.zoom || 1) * (d > 0 ? 1.35 : 1 / 1.35)));
  const s = $('#sld-view svg'); if (s) s.style.width = (100 * S.zoom) + '%';
};
window.switchTab = switchTab;

/* ══ kiểm kê ═══════════════════════════════════════════════ */
function renderInventory() {
  const s = S.data.stats;
  const card = (n, l, sub) => `<div class="sc"><div class="n">${n}</div><div class="l">${l}</div>${sub ? `<div class="s">${sub}</div>` : ''}</div>`;
  const kvRow = (v) => `<tr><td><span class="pill p${v}">${v} kV</span></td>
    <td class="num">${nf(s.lines_by_kv[v] || 0)}</td>
    <td class="num">${nf(s['km_' + v])}</td>
    <td class="num">${nf(S.data.substations.filter((x) => x.lv.includes(+v)).length)}</td></tr>`;

  $('#inv-body').innerHTML = `<div class="doc-inner">
    <h2>Kiểm kê mô hình</h2>
    <p>Toàn bộ số liệu dưới đây đọc trực tiếp từ ${esc(S.data.model)} bằng PowSyBl, không qua bước biên tập nào.</p>
    <div class="stat-cards">
      ${card(nf(s.substations), 'điểm nút', `${nf(s.geolocated)} có toạ độ (${Math.round(100 * s.geolocated / s.substations)}%)`)}
      ${card(nf(s.voltage_levels), 'cấp điện áp', `${nf(s.busbars)} thanh cái`)}
      ${card(nf(s.lines), 'mạch đường dây', `${nf(s.lines_drawn)} vẽ được trên bản đồ`)}
      ${card(nf(s.switches), 'thiết bị đóng cắt', 'máy cắt và dao cách ly')}
      ${card(nf(s.transformers), 'máy biến áp', 'hai cuộn dây')}
      ${card(nf(s.generators), 'tổ máy phát', nf(s.gen_mw) + ' MW đặt')}
      ${card(nf(s.shunts), 'thiết bị bù', 'kháng và tụ')}
      ${card(nf(s.loads), 'nút phụ tải', 'p0 = 0, mô hình tĩnh')}
    </div>

    <h3>Theo cấp điện áp</h3>
    <table><thead><tr><th>Cấp</th><th style="text-align:right">Mạch đường dây</th>
      <th style="text-align:right">km mạch (ước tính)</th><th style="text-align:right">Điểm nút có cấp này</th></tr></thead>
      <tbody>${[500, 220, 110].map(kvRow).join('')}</tbody></table>
    <div class="callout"><p>Số km suy ngược từ điện kháng đã dựng trong mô hình, không phải chiều dài đo được.
      Đây là km mạch: đường dây hai mạch được tính hai lần.</p></div>

    <h3>Cơ cấu nguồn</h3>
    <table><thead><tr><th>Loại nguồn</th><th style="text-align:right">Số tổ máy</th>
      <th style="text-align:right">Công suất đặt (MW)</th><th style="text-align:right">Tỷ trọng</th></tr></thead>
      <tbody>${Object.entries(s.fuel).sort((a, b) => b[1].mw - a[1].mw).map(([k, v]) =>
    `<tr><td><span style="color:${(FUEL[k] || FUEL.OTHER)[0]}">■</span> ${(FUEL[k] || ['', k])[1]}</td>
      <td class="num">${nf(v.n)}</td><td class="num">${nf(v.mw)}</td>
      <td class="num">${(100 * v.mw / s.gen_mw).toFixed(1)}%</td></tr>`).join('')}
      </tbody></table>

    <h3>Phân loại điểm nút</h3>
    <table><thead><tr><th>Loại</th><th style="text-align:right">Số lượng</th></tr></thead><tbody>
      ${Object.entries(s.kinds).map(([k, v]) =>
    `<tr><td>${KIND[k] || k}</td><td class="num">${nf(v)}</td></tr>`).join('')}
    </tbody></table>
    ${S.extra && S.extra.nguon ? `<h3>Nhận định về cơ cấu nguồn</h3><div>${mdToHtml(S.extra.nguon)}</div>` : ''}
    ${regionTable()}
    ${refTable()}
  </div>`;
}

/* đối chiếu theo vùng điều độ và với số liệu A2 đã công bố */
function regionTable() {
  const R = S.data.stats.by_region;
  if (!R || !R.Nam || !R.Nam.diem_nut) return '';
  const cols = ['Bac', 'Trung', 'Nam'];
  const row = (l, f) => `<tr><td>${l}</td>${cols.map((c) => `<td class="num">${nf(f(R[c]))}</td>`).join('')}</tr>`;
  const N = R.Nam;
  // Số liệu A2 công bố (SSO_A2_GioiThieuTongQuan.pptx)
  const A2 = [
    ['Trạm biến áp 500 kV', N.TBA_500, 20], ['Trạm biến áp 220 kV', N.TBA_220, 73],
    ['Trạm biến áp 110 kV', N.TBA_110, 417], ['Đường dây 220 kV', N.DZ_220, 240],
    ['Đường dây 110 kV', N.DZ_110, 765], ['km đường dây 220 kV', N.km_220, 7351],
    ['km đường dây 110 kV', N.km_110, 8994], ['Máy biến áp', N.MBA, 1094],
  ];
  const pct = (a, b) => Math.round(100 * a / b);
  const tag = (p) => p >= 90 && p <= 115 ? 't-ok' : (p >= 70 && p <= 140 ? 't-warn' : 't-bad');

  return `<h3>Phân bố theo vùng điều độ</h3>
    <table><thead><tr><th>Hạng mục</th><th style="text-align:right">Miền Bắc (A1)</th>
      <th style="text-align:right">Miền Trung (A3)</th><th style="text-align:right">Miền Nam (A2)</th></tr></thead><tbody>
      ${row('Điểm nút', (x) => x.diem_nut)}
      ${row('Trạm biến áp 500 kV', (x) => x.TBA_500)}
      ${row('Trạm biến áp 220 kV', (x) => x.TBA_220)}
      ${row('Trạm biến áp 110 kV', (x) => x.TBA_110)}
      ${row('Sân phân phối nhà máy', (x) => x.nha_may)}
      ${row('Trạm cắt', (x) => x.tram_cat)}
      ${row('Mạch 500 kV', (x) => x.DZ_500)}
      ${row('Mạch 220 kV', (x) => x.DZ_220)}
      ${row('Mạch 110 kV', (x) => x.DZ_110)}
      ${row('Máy biến áp', (x) => x.MBA)}
      ${row('Tổ máy phát', (x) => x.to_may)}
      ${row('Công suất đặt (MW)', (x) => x.MW)}
    </tbody></table>
    ${R.khong_ro && R.khong_ro.diem_nut ? `<p>Còn ${nf(R.khong_ro.diem_nut)} điểm nút chưa gán được vùng
      do thiếu toạ độ và thiếu mô tả vị trí.</p>` : ''}

    <h3>Đối chiếu miền Nam với số liệu A2 công bố</h3>
    <p>Cột bên phải lấy từ tài liệu giới thiệu tổng quan của Trung tâm Điều độ Hệ thống điện miền Nam.
      Quy ước đếm của A2: trạm biến áp là trạm có máy biến áp, không tính sân phân phối nhà máy và không
      tính trạm cắt. Mô hình được đếm theo đúng quy ước đó để so sánh công bằng.</p>
    <table><thead><tr><th>Hạng mục</th><th style="text-align:right">Mô hình</th>
      <th style="text-align:right">A2 công bố</th><th style="text-align:right">Độ phủ</th></tr></thead><tbody>
      ${A2.map(([l, a, b]) => `<tr><td>${l}</td><td class="num">${nf(a)}</td><td class="num">${nf(b)}</td>
        <td class="num"><span class="tag ${tag(pct(a, b))}">${pct(a, b)}%</span></td></tr>`).join('')}
    </tbody></table>
    <div class="callout"><p>Đây là phép kiểm chéo độc lập duy nhất hiện có: số liệu A2 không hề tham gia
      vào quá trình dựng mô hình. Chỉ tiêu nào lệch quá xa 100% là chỉ tiêu cần soi lại, hoặc do mô hình
      còn thiếu, hoặc do quy ước đếm chưa khớp.</p></div>`;
}

/* đối chiếu với một mô hình TSO đã số hoá trọn vẹn */
function refTable() {
  if (!S.ref) return '';
  const s = S.data.stats, r = S.ref;
  const rows = [
    ['Trạm và sân phân phối', s.substations, r.substations],
    ['Cấp điện áp', s.voltage_levels, r.voltage_levels],
    ['Thanh cái', s.busbars, r.busbars],
    ['Thiết bị đóng cắt', s.switches, r.switches],
    ['Đường dây', s.lines, r.lines],
    ['Máy biến áp hai cuộn', s.transformers, r.transformers],
    ['Tổ máy phát', s.generators, r.generators],
    ['Nút phụ tải', s.loads, r.loads],
    ['Thiết bị bù', s.shunts, r.shunts],
  ];
  const sw1 = (s.switches / s.substations).toFixed(1), sw2 = (r.switches / r.substations).toFixed(1);
  return `<h3>Đối chiếu với một mô hình đã số hoá trọn vẹn</h3>
    <p>Cột bên phải là một ảnh chụp vận hành thật của lưới truyền tải Pháp (${esc(r.file)}, ${r.size_mb} MB),
      dùng làm mốc so sánh về mức độ chi tiết. Hai cột không cùng bản chất: cột trái là mô hình tham chiếu
      tĩnh dựng từ bản vẽ, cột phải là Point Figé có đầy đủ trạng thái vận hành.</p>
    <table><thead><tr><th>Hạng mục</th><th style="text-align:right">GridTwinVN</th>
      <th style="text-align:right">Point Figé Pháp</th><th style="text-align:right">Tỷ lệ</th></tr></thead><tbody>
      ${rows.map(([l, a, b]) => `<tr><td>${l}</td><td class="num">${nf(a)}</td>
        <td class="num">${nf(b)}</td><td class="num">${Math.round(100 * a / b)}%</td></tr>`).join('')}
      <tr><td>Thiết bị đóng cắt trên mỗi trạm</td><td class="num">${sw1}</td><td class="num">${sw2}</td>
        <td class="num">${Math.round(100 * sw1 / sw2)}%</td></tr>
      <tr><td>Công suất phát ghi trong file</td><td class="num">0 MW</td>
        <td class="num">${nf(r.gen_mw_dispatched)} MW</td><td class="num">—</td></tr>
      <tr><td>Phụ tải ghi trong file</td><td class="num">0 MW</td>
        <td class="num">${nf(r.load_mw)} MW</td><td class="num">—</td></tr>
      <tr><td>Đường dây một chiều</td><td class="num">0</td><td class="num">${r.hvdc}</td><td class="num">—</td></tr>
    </tbody></table>
    <div class="callout"><p>Hai dòng cuối là khoảng cách thực sự giữa hai mô hình. Số lượng phần tử của
      GridTwinVN đã ở mức có thể so sánh được, nhưng toàn bộ trạng thái vận hành vẫn bằng 0. Mật độ thiết
      bị đóng cắt trên mỗi trạm (${sw1} so với ${sw2}) cho thấy mức chi tiết node-breaker của mô hình Việt Nam
      còn thấp hơn, chủ yếu ở các trạm 110 kV mà bản vẽ chỉ thể hiện ở dạng rút gọn.</p></div>`;
}

/* ══ chất lượng dữ liệu ════════════════════════════════════ */
function renderQA() {
  const s = S.data.stats;
  const conf = { high: 0, medium: 0, low: 0 };
  S.data.substations.forEach((x) => { if (x.lat != null) conf[x.conf === 'high' ? 'high' : x.conf === 'low' ? 'low' : 'medium']++; });
  const noGeo = s.substations - s.geolocated;

  $('#qa-body').innerHTML = `<div class="doc-inner">
    <h2>Chất lượng và nguồn gốc dữ liệu</h2>
    <div class="callout"><p><b>Đây là mô hình tham chiếu tĩnh, không phải ảnh chụp vận hành.</b>
      Toàn bộ công suất phát và phụ tải bằng 0. Không có trạng thái máy cắt thực tế, không có kết quả
      tính trào lưu công suất. Muốn có Point Figé phải có SCADA cộng bộ ước lượng trạng thái.</p></div>

    <h3>Phân tầng nguồn gốc từng lớp dữ liệu</h3>
    <table><thead><tr><th>Lớp dữ liệu</th><th>Nguồn</th><th>Độ tin cậy</th></tr></thead><tbody>
      <tr><td>Danh mục trạm, đường dây, mã ngăn</td><td>Đọc trực tiếp từ bản vẽ NSMO</td><td><span class="tag t-ok">đọc trực tiếp</span></td></tr>
      <tr><td>Sơ đồ thanh cái (3/2, hai thanh cái, một thanh cái)</td><td>Đọc trực tiếp từ bản vẽ</td><td><span class="tag t-ok">đọc trực tiếp</span></td></tr>
      <tr><td>Mã dây dẫn, chiều dài tuyến</td><td>Nhãn in trên bản vẽ</td><td><span class="tag t-ok">đọc trực tiếp</span></td></tr>
      <tr><td>Công suất máy biến áp, tổ máy</td><td>Nhãn MVA và MW trên bản vẽ</td><td><span class="tag t-ok">đọc trực tiếp</span></td></tr>
      <tr><td>Điện trở, điện kháng, dung dẫn đường dây</td><td>Suy từ mã dây và cấp điện áp theo bảng tra</td><td><span class="tag t-warn">ước lượng</span></td></tr>
      <tr><td>Điện áp ngắn mạch máy biến áp</td><td>Giá trị điển hình theo cấp và công suất</td><td><span class="tag t-warn">ước lượng</span></td></tr>
      <tr><td>Toạ độ địa lý</td><td>OpenStreetMap và tra cứu địa danh</td><td><span class="tag t-warn">ngoài bản vẽ</span></td></tr>
      <tr><td>Trạng thái vận hành, trào lưu công suất</td><td>Không có trên bản vẽ</td><td><span class="tag t-bad">thiếu</span></td></tr>
    </tbody></table>

    <h3>Độ phủ toạ độ</h3>
    <div class="stat-cards">
      <div class="sc"><div class="n">${nf(s.geolocated)}</div><div class="l">điểm nút có toạ độ</div>
        <div class="s">${Math.round(100 * s.geolocated / s.substations)}% tổng số</div></div>
      <div class="sc"><div class="n">${nf(conf.high)}</div><div class="l">tin cậy cao</div><div class="s">tra được vị trí cụ thể</div></div>
      <div class="sc"><div class="n">${nf(conf.medium)}</div><div class="l">tin cậy vừa</div><div class="s">tâm huyện hoặc suy từ lân cận</div></div>
      <div class="sc"><div class="n">${nf(conf.low)}</div><div class="l">tin cậy thấp</div><div class="s">chỉ biết tới cấp tỉnh</div></div>
      <div class="sc"><div class="n">${nf(noGeo)}</div><div class="l">chưa có toạ độ</div><div class="s">không hiển thị trên bản đồ</div></div>
      <div class="sc"><div class="n">${nf(s.lines - s.lines_drawn)}</div><div class="l">mạch chưa vẽ được</div><div class="s">thiếu toạ độ một đầu</div></div>
      <div class="sc"><div class="n">${nf(s.lines_suspect || 0)}</div><div class="l">tuyến nghi ghép sai</div><div class="s">dài bất thường so với cấp áp</div></div>
      <div class="sc"><div class="n">${nf(s.jittered || 0)}</div><div class="l">điểm nút bị xếp vòng</div><div class="s">trùng khít toạ độ tâm huyện</div></div>
    </div>
    <div class="callout"><p>Khi nhiều trạm cùng chỉ tra được tới cấp huyện, chúng nhận đúng một toạ độ
      tâm huyện và sẽ che khuất nhau trên bản đồ. ${nf(s.jittered || 0)} điểm nút như vậy được xếp thành
      vòng tròn bán kính khoảng 700 m quanh điểm gốc để nhìn thấy được. Đây là thao tác hiển thị, không
      phải thông tin vị trí mới. Các trạm này luôn mang độ tin cậy vừa hoặc thấp và bảng chi tiết của
      chúng ghi rõ điều đó.</p></div>

    <h3>Tuyến nghi ghép sai đầu nối</h3>
    <p>Chiều dài đường chim bay giữa hai đầu vượt xa mức hợp lý của cấp điện áp
      (ngưỡng: 110 kV trên 150 km, 220 kV trên 300 km, 500 kV trên 600 km). Nguyên nhân gần như luôn
      là trùng tên địa danh khi khâu biên giữa các ô ảnh, ví dụ Hoà Bình tỉnh phía bắc bị ghép với
      Hoà Bình huyện Bạc Liêu, hay Sơn Tây Hà Nội bị ghép với Sơn Tây Quảng Ngãi.
      Các tuyến này bị ẩn mặc định trên bản đồ, bật lại bằng ô "Hiện tuyến nghi ghép sai".</p>
    ${(S.susp || []).length ? `<table><thead><tr><th>Cấp</th><th>Đầu A</th><th>Đầu B</th>
      <th style="text-align:right">km chim bay</th></tr></thead><tbody>
      ${S.susp.slice(0, 60).map((l) => `<tr><td><span class="pill p${l.kv}">${l.kv}</span></td>
        <td>${esc(l.a)}<br><small style="color:#61728f">${esc(l.a_place)}</small></td>
        <td>${esc(l.b)}<br><small style="color:#61728f">${esc(l.b_place)}</small></td>
        <td class="num">${nf(l.km)}</td></tr>`).join('')}
      </tbody></table>
      ${S.susp.length > 60 ? `<p>và ${S.susp.length - 60} tuyến khác, xem đầy đủ ở <code>data/suspect_lines.json</code>.</p>` : ''}`
      : '<p>Không phát hiện tuyến nào vượt ngưỡng.</p>'}

    ${S.extra && S.extra.chatluong ? `<h3>Cảnh báo do hội đồng kiểm định phát hiện</h3><div>${mdToHtml(S.extra.chatluong)}</div>` : ''}

    <h3>Những gì mô hình chưa làm được</h3>
    <ul>
      <li>Máy biến áp tự ngẫu đang dựng ở dạng hai cuộn dây. Trên 2.578 bản ghi máy biến áp đọc được,
        chỉ 26 bản ghi ghi rõ ba cấp điện áp, phần còn lại bản vẽ chỉ ghi 220/110 hoặc 500/220. Muốn
        dựng cuộn thứ ba phải áp một giả định ngành nghề chứ không đọc được từ bản vẽ, nên tạm để nguyên.</li>
      <li>Một số cụm lưới còn tách rời nhau do chưa khâu được biên giữa các ô ảnh khi trích xuất.</li>
      <li>Giới hạn dòng điện vận hành (IST) chưa được nạp, cần số liệu thí nghiệm từ đơn vị truyền tải.</li>
      <li>Chưa có mô hình động của máy phát nên không chạy được đánh giá ổn định.</li>
    </ul>
  </div>`;
}

/* ══ thuyết minh ═══════════════════════════════════════════ */
function renderDoc() {
  const t = S.extra && S.extra.thuyetminh;
  $('#doc-body').innerHTML = `<div class="doc-inner">${t ? mdToHtml(t) : `
    <h2>GridTwinVN</h2>
    <p>Bản trực quan tĩnh của mô hình <b>${esc(S.data.model)}</b>, tái dựng từ ${esc(S.data.source)}.</p>
    <div class="callout info"><p>${esc(S.data.nature)}</p></div>
    <h3>Quy ước màu</h3>
    <p>Màu đường dây theo đúng quy ước của chính bản vẽ NSMO: xanh lá là 500 kV, đỏ là 220 kV,
       xanh dương là 110 kV. Nét đứt là công trình dự kiến vào vận hành năm 2025.</p>
    <h3>Cách sử dụng</h3>
    <ul>
      <li>Bấm vào một điểm nút để xem thiết bị bên trong, mã ngăn đọc từ bản vẽ và các mạch đấu nối.</li>
      <li>Tab Sơ đồ trạm chứa thư viện sơ đồ một sợi dựng bằng PowSyBl từ chính topology node-breaker.</li>
      <li>Tab Kiểm kê là bảng đếm đầy đủ, đọc trực tiếp từ file mô hình.</li>
      <li>Tab Chất lượng dữ liệu ghi rõ lớp nào đọc từ bản vẽ, lớp nào là ước lượng, lớp nào còn thiếu.</li>
    </ul>`}
    ${S.extra && S.extra.hanhlang500 ? `<h2>Hành lang 500 kV</h2><div>${mdToHtml(S.extra.hanhlang500)}</div>` : ''}
    ${S.extra && S.extra.phutai ? `<h2>Phụ tải công nghiệp đấu nối trực tiếp</h2><div>${mdToHtml(S.extra.phutai)}</div>` : ''}
  </div>`;
}

/* ══ markdown tối giản ═════════════════════════════════════ */
function mdToHtml(md) {
  const lines = String(md).split('\n');
  let out = '', inTable = false, inList = false, inCode = false;
  const flush = () => { if (inTable) { out += '</tbody></table>'; inTable = false; } if (inList) { out += '</ul>'; inList = false; } };
  const inline = (s) => esc(s)
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/`(.+?)`/g, '<code style="background:#1a2333;padding:1px 5px;border-radius:4px;font-size:12px">$1</code>');

  for (let i = 0; i < lines.length; i++) {
    const l = lines[i], t = l.trim();
    if (t.startsWith('```')) { inCode = !inCode; flush(); out += inCode ? '<pre style="background:#0f1622;border:1px solid #1e2a3d;border-radius:8px;padding:12px;overflow:auto;font-size:12px;color:#9fb3d0">' : '</pre>'; continue; }
    if (inCode) { out += esc(l) + '\n'; continue; }
    if (!t) { flush(); continue; }
    if (/^#{1,6}\s/.test(t)) { flush(); const n = t.match(/^#+/)[0].length; out += `<h${Math.min(n + 1, 4)}>${inline(t.replace(/^#+\s*/, ''))}</h${Math.min(n + 1, 4)}>`; continue; }
    if (/^\|/.test(t)) {
      const cells = t.split('|').slice(1, -1).map((c) => c.trim());
      if (/^[\s|:-]+$/.test(t)) continue;
      if (!inTable) { out += `<table><thead><tr>${cells.map((c) => `<th>${inline(c)}</th>`).join('')}</tr></thead><tbody>`; inTable = true; }
      else out += `<tr>${cells.map((c) => `<td>${inline(c)}</td>`).join('')}</tr>`;
      continue;
    }
    if (inTable) { out += '</tbody></table>'; inTable = false; }
    if (/^[-*]\s/.test(t) || /^\d+\.\s/.test(t)) {
      if (!inList) { out += '<ul>'; inList = true; }
      out += `<li>${inline(t.replace(/^([-*]|\d+\.)\s*/, ''))}</li>`; continue;
    }
    if (inList) { out += '</ul>'; inList = false; }
    out += `<p>${inline(t)}</p>`;
  }
  flush();
  return out;
}

boot().catch((e) => {
  $('#loading').innerHTML = `<p style="color:#f87171">Không nạp được dữ liệu: ${esc(e.message)}</p>
    <p style="font-size:12px">Cần chạy <code>python build/export_data.py</code> trước, và mở trang qua máy chủ web
    (ví dụ <code>python -m http.server</code>) chứ không mở trực tiếp bằng file://</p>`;
});
