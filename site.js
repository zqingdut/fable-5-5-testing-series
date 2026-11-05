// Fable 5.5 Testing Series — waterfall front-end.
// Data source: data/cases.json (single source of truth, auto-maintained).
(function () {
  var grid = document.getElementById('grid');
  var countEl = document.getElementById('count');
  var searchEl = document.getElementById('search');
  var activeCat = 'all';
  var allCases = [];

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

  function card(item) {
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
      '<details><summary>查看 Prompt</summary><pre>' + esc(item.prompt || '未公开') + '</pre></details>' +
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
    grid.innerHTML = rows.length
      ? rows.map(card).join('')
      : '<p class="empty">没有符合条件的案例。</p>';
    countEl.textContent = '共 ' + allCases.length + ' 条案例' +
      (rows.length !== allCases.length ? '（显示 ' + rows.length + ' 条）' : '');
  }

  document.getElementById('filters').addEventListener('click', function (e) {
    var btn = e.target.closest('.pill');
    if (!btn) return;
    document.querySelectorAll('.pill').forEach(function (p) { p.classList.remove('active'); });
    btn.classList.add('active');
    activeCat = btn.getAttribute('data-cat');
    render();
  });
  searchEl.addEventListener('input', render);

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
