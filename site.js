// Fable 5.5 Testing Series — waterfall front-end.
// Data source: data/cases.json (single source of truth, auto-maintained).
// Layout: JS-managed flex columns. Expanding a card's prompt only grows
// that card's own column — no global reflow, no width jumps.
(function () {
  var grid = document.getElementById('grid');
  var countEl = document.getElementById('count');
  var searchEl = document.getElementById('search');
  var activeCat = 'all';
  var allCases = [];
  var lastColCount = 0;

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function fmtCost(v) {
    if (v === '' || v == null) return '';
    if (typeof v === 'number') return '$' + v;
    var s = String(v);
    if (s.charAt(0) === '~') return '~$' + s.slice(1);
    return s.indexOf('$') >= 0 ? s : '$' + s;
  }

  function colCount() {
    var w = grid.clientWidth || window.innerWidth;
    if (w >= 1000) return 3;
    if (w >= 640) return 2;
    return 1;
  }

  function cardHTML(item) {
    var metaBits = [esc(item.author), esc(item.created_at)];
    if (item.duration_sec) metaBits.push(esc(item.duration_sec) + 's');
    if (item.work_time) metaBits.push('耗时 ' + esc(item.work_time));
    var cost = fmtCost(item.cost_usd);
    if (cost) metaBits.push('成本 ' + esc(cost));

    var chips = (item.tech_stack || [])
      .map(function (t) { return '<span class="chip">' + esc(t) + '</span>'; })
      .join('');

    var demo = item.demo_url
      ? '<a href="' + esc(item.demo_url) + '" target="_blank" rel="noopener">🕹️ 在线试玩</a>'
      : '';

    return (
      '<article class="card">' +
      (item.preview_webp
        ? '<img class="preview" loading="lazy" src="' + esc(item.preview_webp) + '" alt="' + esc(item.title) + ' 预览" />'
        : '') +
      '<div class="body">' +
      '<h3>' + esc(item.title) +
      (item.verification ? '<span class="badge">' + esc(item.verification) + '</span>' : '') +
      '</h3>' +
      '<div class="meta">' + metaBits.join(' · ') + '</div>' +
      '<p class="summary">' + esc(item.summary) + '</p>' +
      (chips ? '<div class="chips">' + chips + '</div>' : '') +
      '<button class="prompt-toggle" type="button" aria-expanded="false">' +
      '<span class="arrow">▸</span>查看 Prompt</button>' +
      '<div class="prompt-wrap"><div class="prompt-inner"><pre>' +
      esc(item.prompt || '未公开') +
      '</pre></div></div>' +
      '<div class="links">' +
      '<a href="' + esc(item.tweet_url) + '" target="_blank" rel="noopener">🔗 原推文</a>' +
      demo +
      '</div>' +
      '</div></article>'
    );
  }

  function render() {
    var q = (searchEl.value || '').trim().toLowerCase();
    var rows = allCases.filter(function (c) {
      if (activeCat !== 'all' && c.category !== activeCat) return false;
      if (!q) return true;
      var hay = [c.title, c.author, c.summary, (c.tech_stack || []).join(' ')]
        .join(' ')
        .toLowerCase();
      return hay.indexOf(q) >= 0;
    });

    countEl.textContent = '共 ' + allCases.length + ' 条案例' +
      (rows.length !== allCases.length ? '（显示 ' + rows.length + ' 条）' : '');

    if (!rows.length) {
      grid.innerHTML = '<p class="empty">没有符合条件的案例。</p>';
      lastColCount = 0;
      return;
    }

    var n = colCount();
    lastColCount = n;
    grid.innerHTML = '';
    var cols = [];
    for (var i = 0; i < n; i++) {
      var col = document.createElement('div');
      col.className = 'col';
      grid.appendChild(col);
      cols.push(col);
    }
    // Append each card to the currently shortest column.
    rows.forEach(function (item) {
      var target = cols[0];
      for (var j = 1; j < cols.length; j++) {
        if (cols[j].offsetHeight < target.offsetHeight) target = cols[j];
      }
      var t = document.createElement('template');
      t.innerHTML = cardHTML(item).trim();
      target.appendChild(t.content.firstElementChild);
    });
  }

  // Prompt expand/collapse (event delegation; animation is pure CSS).
  grid.addEventListener('click', function (e) {
    var btn = e.target.closest('.prompt-toggle');
    if (!btn) return;
    var wrap = btn.parentElement.querySelector('.prompt-wrap');
    var open = wrap.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  document.getElementById('filters').addEventListener('click', function (e) {
    var btn = e.target.closest('.pill');
    if (!btn) return;
    document.querySelectorAll('.pill').forEach(function (p) { p.classList.remove('active'); });
    btn.classList.add('active');
    activeCat = btn.getAttribute('data-cat');
    render();
  });
  searchEl.addEventListener('input', render);

  // Re-distribute only when the column count actually changes.
  var resizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      if (allCases.length && colCount() !== lastColCount) render();
    }, 150);
  });

  fetch('data/cases.json')
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      allCases = Array.isArray(data) ? data : [];
      render();
    })
    .catch(function (err) {
      grid.innerHTML = '<p class="empty">案例数据加载失败（' + esc(err.message) + '），请到 GitHub 仓库查看。</p>';
    });
})();
