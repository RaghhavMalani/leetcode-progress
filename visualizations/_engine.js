/* ============================================================
   leetcode-progress · shared visualization engine
   ------------------------------------------------------------
   A tiny step-player. Every problem page supplies:
     - the exact source of the solution in this repo
     - a build() that replays that source and emits one event
       per meaningful step (line number + narration + state views)
     - theory: how to recognise the pattern, the template, the
       traps, the variants, and how to think about it
   The engine does the rest: highlight, scrub, draw, narrate.
   ============================================================ */
(function (global) {
"use strict";

var LV = {};

/* ------------------------------------------------------------
   0. helpers
   ------------------------------------------------------------ */
function esc(s){ return String(s).replace(/[&<>]/g, function(c){ return c==='&'?'&amp;':(c==='<'?'&lt;':'&gt;'); }); }
function el(tag, cls, html){ var d=document.createElement(tag); if(cls) d.className=cls; if(html!=null) d.innerHTML=html; return d; }
LV.esc = esc;

/* syntax highlighting — python / c-family, good enough to read by */
var KW = /\b(class|def|if|elif|else|return|while|for|in|not|or|and|None|True|False|lambda|break|continue|import|from|global|nonlocal|try|except|with|as|yield|pass|del|is|public|private|void|int|long|bool|string|vector|auto|new|const|struct|nullptr|NULL|sort|static|float|double|char)\b/g;
var FNS = /\b([a-zA-Z_][a-zA-Z0-9_]*)(?=\()/g;
function hl(line){
  var store=[], s=esc(line);
  function keep(html){ store.push(html); return '\u0002'+String.fromCharCode(0xE000+store.length-1)+'\u0003'; }
  s = s.replace(/(#[^\n]*|\/\/[^\n]*)/g, function(m){ return keep('<span class="cm">'+m+'</span>'); });
  s = s.replace(/("""[\s\S]*?"""|\x27\x27\x27[\s\S]*?\x27\x27\x27|"[^"]*"|\x27[^\x27]*\x27)/g, function(m){ return keep('<span class="str">'+m+'</span>'); });
  s = s.replace(FNS, function(m){ return keep('<span class="fn">'+m+'</span>'); });
  s = s.replace(KW, function(m){ return keep('<span class="kw">'+m+'</span>'); });
  s = s.replace(/\b\d+(\.\d+)?\b/g, function(m){ return keep('<span class="num">'+m+'</span>'); });
  return s.replace(/\u0002([\uE000-\uF8FF])\u0003/g, function(m,ch){ return store[ch.charCodeAt(0)-0xE000]; });
}

/* ------------------------------------------------------------
   1. view constructors — each returns a plain descriptor object
      that render() knows how to draw.
   ------------------------------------------------------------ */

/* array / string of cells.
   marks: { index : 'cls' }  or  { index : ['cls','ptrLabel'] }
   opts:  { idx:true, ptrs:{index:'l,r'}, note:'' }                       */
LV.arr = function (name, vals, marks, opts) {
  return { k:'arr', name:name, vals:(vals||[]).slice(), marks:marks||{}, o:opts||{} };
};
/* histogram bars. vals = heights, fill = {i: extraUnitsOfWater} */
LV.bars = function (name, vals, marks, fill, opts) {
  return { k:'bars', name:name, vals:vals.slice(), marks:marks||{}, fill:fill||{}, o:opts||{} };
};
/* hash map / set / counter. pairs = [[k,v],...] or ['a','b'] for a set */
LV.kv = function (name, pairs, marks, opts) {
  return { k:'kv', name:name, pairs:(pairs||[]).map(function(p){ return Array.isArray(p)?p:[p,null]; }),
           marks:marks||{}, o:opts||{} };
};
/* list / stack / queue. vertical:true stacks them bottom-up */
LV.seq = function (name, vals, marks, opts) {
  return { k:'seq', name:name, vals:(vals||[]).slice(), marks:marks||{}, o:opts||{} };
};
/* linked list. nodes = [{v:val, id:'a', cls:'', dummy:true}], labels = {id:'slow fast'} */
LV.ll = function (name, nodes, labels, opts) {
  return { k:'ll', name:name, nodes:(nodes||[]).map(function(n){ return Object.assign({},n); }),
           labels:labels||{}, o:opts||{} };
};
/* 2D matrix. marks = { 'r,c':'cls' }, opts.head = true for index headers */
LV.grid = function (name, rows, marks, opts) {
  return { k:'grid', name:name, rows:rows.map(function(r){ return r.slice(); }), marks:marks||{}, o:opts||{} };
};
/* call stack frames */
LV.frames = function (name, vals, opts) {
  return { k:'frames', name:name, vals:(vals||[]).slice(), o:opts||{} };
};
/* recursion tree — pass a treeBuilder */
LV.tree = function (tb, cur, opts) {
  return { k:'tree', tb:tb, cur:cur, max:tb.nodes.length-1, o:opts||{} };
};
/* binary tree — nodes = [{id,val,l,r}], marks = {id:'cls'}, labels = {id:'text'} */
LV.btree = function (name, nodes, root, marks, labels, opts) {
  return { k:'btree', name:name, nodes:nodes, root:root, marks:marks||{}, labels:labels||{}, o:opts||{} };
};
/* free-form html row, for anything the above doesn't cover */
LV.html = function (name, htmlStr) { return { k:'html', name:name, html:htmlStr }; };

/* ------------------------------------------------------------
   2. recursion tree builder
   ------------------------------------------------------------ */
LV.treeBuilder = function (nodeW, nodeH, gapX, gapY) {
  var tb = { nodes:[], W:nodeW||58, H:nodeH||28, gx:gapX||68, gy:gapY||52, laid:false };
  tb.add = function (parent, label, sub, frame) {
    var n = { id:tb.nodes.length, label:label, sub:sub||null, frame:frame||label,
              p:(parent===undefined?null:parent), ch:[], dead:null,
              d:(parent===undefined||parent===null?0:tb.nodes[parent].d+1) };
    tb.nodes.push(n);
    if (n.p !== null) tb.nodes[n.p].ch.push(n.id);
    return n.id;
  };
  tb.kill = function (id, step) { tb.nodes[id].dead = step; };
  tb.win  = function (id, step) { tb.nodes[id].won  = step; };
  tb.chain = function (id) { var c=[]; while(id!==null&&id!==undefined){ c.push(id); id=tb.nodes[id].p; } return c; };
  return tb;
};

/* ------------------------------------------------------------
   3. trace recorder
   ------------------------------------------------------------ */
LV.trace = function () {
  var T = { events:[], out:[] };
  /* line   : 1-based line number in spec.src
     type   : call | push | pop | found | prune | info | done | ok | bad | dup
     msg     : narration (plain text, backtick-code allowed)
     vars    : string of html for the top strip, or array of strings
     views   : array of view descriptors                                   */
  T.step = function (line, type, msg, vars, views) {
    T.events.push({ line:line, type:type, msg:msg,
      vars: (Array.isArray(vars)? vars : (vars?[vars]:[])),
      views: views||[], out: T.out.slice() });
    return T.events.length-1;
  };
  T.save = function (v) { T.out.push(v); };
  return T;
};

/* ------------------------------------------------------------
   4. renderers
   ------------------------------------------------------------ */
function markOf(m, key){
  var v = m[key];
  if (v === undefined) return {c:'', t:''};
  if (typeof v === 'string') return {c:v, t:''};
  return {c:v.c||'', t:v.t||''};
}

function drawArr(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="cells">';
  if (!v.vals.length) h += '<span class="empty">empty</span>';
  for (var i=0;i<v.vals.length;i++){
    var m = markOf(v.marks, i);
    var ptr = (v.o.ptrs && v.o.ptrs[i]) ? v.o.ptrs[i] : (m.t||'');
    var pcls = (v.o.ptrCls && v.o.ptrCls[i]) ? ' '+v.o.ptrCls[i] : '';
    h += '<div class="cellwrap">';
    h += '<div class="ptr'+pcls+'">'+esc(ptr)+'</div>';
    h += '<div class="cell '+m.c+'">'+esc(v.vals[i])+'</div>';
    h += v.o.idx===false ? '' : '<div class="idx">'+i+'</div>';
    h += '</div>';
  }
  h += '</div>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawBars(v){
  var max = Math.max.apply(null, v.vals.concat([1]));
  var unit = Math.max(9, Math.min(17, Math.floor(84/max)));
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="bars">';
  for (var i=0;i<v.vals.length;i++){
    var m = markOf(v.marks, i), w = v.fill[i]||0;
    h += '<div class="barwrap"><div class="ptr">'+esc(m.t||'')+'</div><div class="barcol">';
    if (w>0) h += '<div class="bseg water" style="height:'+(w*unit)+'px"></div>';
    if (v.vals[i]>0) h += '<div class="bseg solid '+(m.c==='hot'?'hot':'')+'" style="height:'+(v.vals[i]*unit)+'px"></div>';
    h += '</div><div class="cell '+m.c+'" style="min-width:24px;height:22px;font-size:11px">'+v.vals[i]+'</div>';
    h += '<div class="idx">'+i+'</div></div>';
  }
  h += '</div>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawKv(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="kv">';
  if (!v.pairs.length) h += '<span class="empty">'+(v.o.emptyText||'empty')+'</span>';
  v.pairs.forEach(function(p){
    var m = markOf(v.marks, p[0]);
    h += '<span class="pair '+m.c+'"><b>'+esc(p[0])+'</b>'+(p[1]===null?'':' : '+esc(p[1]))+'</span>';
  });
  h += '</div>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawSeq(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="seq'+(v.o.vert?' vert':'')+'">';
  if (!v.vals.length) h += '<span class="empty">'+(v.o.emptyText||'empty')+'</span>';
  v.vals.forEach(function(x,i){
    var m = markOf(v.marks, i);
    var top = (v.o.top && i===v.vals.length-1) ? ' top' : '';
    h += '<span class="item '+m.c+top+'">'+esc(x)+'</span>';
  });
  h += '</div>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawLl(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="ll">';
  if (!v.nodes.length) h += '<span class="empty">null</span>';
  v.nodes.forEach(function(n,i){
    if (i) h += '<div class="arrow'+(n.on?' on':'')+'">'+(n.back?'⇄':'→')+'</div>';
    var lab = v.labels[n.id]||'';
    h += '<div class="node"><div class="nlab">'+esc(lab)+'</div>'+
         '<div class="nbox '+(n.cls||'')+(n.dummy?' dummy':'')+'">'+esc(n.v)+'</div></div>';
  });
  if (v.o.nullTail!==false) h += '<div class="arrow">→</div><div class="node"><div class="nlab">'+
     esc(v.labels['null']||'')+'</div><div class="nbox dummy">∅</div></div>';
  h += '</div>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawGrid(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><table class="mx">';
  if (v.o.head){
    h += '<tr><th></th>';
    for (var c=0;c<v.rows[0].length;c++) h += '<th>'+c+'</th>';
    h += '</tr>';
  }
  v.rows.forEach(function(row,r){
    h += '<tr>';
    if (v.o.head) h += '<th>'+r+'</th>';
    row.forEach(function(cell,c){
      var m = markOf(v.marks, r+','+c);
      h += '<td class="'+m.c+'">'+esc(cell)+'</td>';
    });
    h += '</tr>';
  });
  h += '</table>';
  if (v.o.note) h += '<div class="vnote">'+v.o.note+'</div>';
  return h;
}

function drawFrames(v){
  var h = '<div class="vname">'+esc(v.name)+'</div><div class="frames">';
  if (!v.vals.length) h += '<span class="empty">no active frames</span>';
  v.vals.forEach(function(f,i){
    h += '<div class="frame'+(i===v.vals.length-1?' top':'')+'">'+esc(f)+'</div>';
  });
  h += '</div>';
  return h;
}

function layoutTree(tb){
  if (tb.laid) return;
  var leaf = 0, maxd = 0;
  (function lay(id){
    var n = tb.nodes[id];
    maxd = Math.max(maxd, n.d);
    if (!n.ch.length) n.px = leaf++;
    else { n.ch.forEach(lay); n.px = (tb.nodes[n.ch[0]].px + tb.nodes[n.ch[n.ch.length-1]].px)/2; }
  })(0);
  var m = tb.W/2 + 12;
  tb.Wpx = Math.max(400, m*2 + (leaf-1)*tb.gx);
  tb.Hpx = 22 + maxd*tb.gy + tb.H/2 + 16;
  tb.nodes.forEach(function(n){ n.x = m + n.px*tb.gx; n.y = 22 + n.d*tb.gy + tb.H/2; });
  tb.laid = true;
}

function drawTree(v, stepIdx){
  var tb = v.tb; layoutTree(tb);
  var path = {}, t = v.cur;
  while (t!==null && t!==undefined){ path[t]=1; t = tb.nodes[t].p; }
  var s = '<svg viewBox="0 0 '+tb.Wpx+' '+tb.Hpx+'" width="'+tb.Wpx+'" height="'+tb.Hpx+
          '" style="width:'+tb.Wpx+'px" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="recursion tree">';
  tb.nodes.forEach(function(n){
    if (n.p===null) return;
    var pn = tb.nodes[n.p], live = n.id <= v.max;
    var col = !live ? '#1b2230' : (path[n.id] ? '#5ec8f2' : '#2a3446');
    s += '<path d="M'+pn.x+' '+(pn.y+tb.H/2)+' C '+pn.x+' '+(pn.y+tb.H/2+18)+', '+n.x+' '+(n.y-tb.H/2-18)+
         ', '+n.x+' '+(n.y-tb.H/2)+'" fill="none" stroke="'+col+'" stroke-width="'+(path[n.id]?1.9:1)+'"/>';
  });
  tb.nodes.forEach(function(n){
    var live = n.id<=v.max, cur = n.id===v.cur;
    var dead = n.dead!==null && n.dead!==undefined && stepIdx>=n.dead;
    var won  = n.won !==null && n.won !==undefined && stepIdx>=n.won;
    var fill='none', stroke='#232c3c', tc='#333d4d', sub='#2a3242', sw=1, dash=' stroke-dasharray="3 3"';
    if (live){ dash=''; fill='#151b27'; stroke='#2e3a4e'; tc='#94a0b4'; sub='#5b6679'; }
    if (live && path[n.id]){ stroke='#5ec8f2'; tc='#cbe9f8'; }
    if (dead){ fill='#241318'; stroke='#7a3b40'; tc='#e0868c'; sub='#a15c60'; }
    if (won){ fill='#102a1e'; stroke='#4ec98a'; tc='#8ee0b1'; sub='#4d8a68'; }
    if (cur){ fill = won?'#123a27':(dead?'#3a181e':'#0d3a4e');
              stroke = won?'#4ec98a':(dead?'#e0686e':'#5ec8f2'); tc='#eaf7ff'; sw=2.2; }
    var yTop = n.sub ? n.y-1 : n.y+4.2;
    s += '<g><title>'+esc(n.frame)+'</title>';
    s += '<rect x="'+(n.x-tb.W/2)+'" y="'+(n.y-tb.H/2)+'" width="'+tb.W+'" height="'+tb.H+
         '" rx="6" fill="'+fill+'" stroke="'+stroke+'" stroke-width="'+sw+'"'+dash+'/>';
    s += '<text x="'+n.x+'" y="'+yTop+'" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="11" fill="'+tc+'">'+esc(n.label)+'</text>';
    if (n.sub) s += '<text x="'+n.x+'" y="'+(n.y+10)+'" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="8.5" fill="'+sub+'">'+esc(n.sub)+'</text>';
    s += '</g>';
  });
  s += '</svg>';
  return '<div class="vname">'+(v.o.name||'recursion tree')+'</div><div class="treescroll">'+s+'</div>';
}

function drawBtree(v){
  var idx = {}; v.nodes.forEach(function(n){ idx[n.id]=n; });
  var leaf = 0, maxd = 0;
  (function lay(id, d){
    var n = idx[id]; if (!n) return;
    n.d = d; maxd = Math.max(maxd,d);
    if (n.l) lay(n.l, d+1);
    if (!n.l && !n.r) n.px = leaf++;
    if (n.r) lay(n.r, d+1);
    if (n.l || n.r){
      var a = n.l?idx[n.l].px:null, b = n.r?idx[n.r].px:null;
      n.px = (a!==null&&b!==null) ? (a+b)/2 : (a!==null?a+0.5:b-0.5);
    }
  })(v.root, 0);
  var W=36,H=30,gx=54,gy=54, m=W/2+14;
  var Wpx = Math.max(280, m*2 + leaf*gx), Hpx = 20 + maxd*gy + H/2 + 14;
  v.nodes.forEach(function(n){ n.x = m + n.px*gx; n.y = 20 + n.d*gy + H/2; });
  var s = '<svg viewBox="0 0 '+Wpx+' '+Hpx+'" width="'+Wpx+'" height="'+Hpx+'" style="width:'+Wpx+'px" xmlns="http://www.w3.org/2000/svg">';
  v.nodes.forEach(function(n){
    [n.l,n.r].forEach(function(c){
      if (!c || !idx[c]) return;
      var ch = idx[c], on = v.marks[c] && v.marks[c]!=='dim';
      s += '<line x1="'+n.x+'" y1="'+(n.y+H/2)+'" x2="'+ch.x+'" y2="'+(ch.y-H/2)+
           '" stroke="'+(on?'#5ec8f2':'#2a3446')+'" stroke-width="'+(on?1.8:1)+'"/>';
    });
  });
  var pal = { hot:['#0d3a4e','#5ec8f2','#eaf7ff'], good:['#102a1e','#4ec98a','#8ee0b1'],
              bad:['#241318','#7a3b40','#e0868c'], warn:['#2a2110','#7a5a1e','#f3cf8a'],
              vio:['#20163a','#5b4a9e','#c3b0f5'], dim:['none','#232c3c','#333d4d'],
              '':['#151b27','#2e3a4e','#94a0b4'] };
  v.nodes.forEach(function(n){
    var c = pal[v.marks[n.id]||''] || pal[''];
    s += '<g><circle cx="'+n.x+'" cy="'+n.y+'" r="15" fill="'+c[0]+'" stroke="'+c[1]+'" stroke-width="'+(v.marks[n.id]==='hot'?2.2:1.3)+'"/>';
    s += '<text x="'+n.x+'" y="'+(n.y+4)+'" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="11.5" fill="'+c[2]+'">'+esc(n.val)+'</text>';
    if (v.labels[n.id]) s += '<text x="'+n.x+'" y="'+(n.y+29)+'" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="9" fill="#5b6679">'+esc(v.labels[n.id])+'</text>';
    s += '</g>';
  });
  s += '</svg>';
  return '<div class="vname">'+esc(v.name)+'</div><div class="treescroll">'+s+'</div>';
}

function drawView(v, stepIdx){
  switch (v.k){
    case 'arr':    return drawArr(v);
    case 'bars':   return drawBars(v);
    case 'kv':     return drawKv(v);
    case 'seq':    return drawSeq(v);
    case 'll':     return drawLl(v);
    case 'grid':   return drawGrid(v);
    case 'frames': return drawFrames(v);
    case 'tree':   return drawTree(v, stepIdx);
    case 'btree':  return drawBtree(v);
    case 'html':   return '<div class="vname">'+esc(v.name)+'</div>'+v.html;
  }
  return '';
}

/* ------------------------------------------------------------
   5. theory block
   ------------------------------------------------------------ */
function theoryHtml(th, cx){
  if (!th) return '';
  var h = '<div class="theory"><div class="sec"><h3>The pattern behind this problem</h3>';
  if (th.idea) h += '<div class="big">'+th.idea+'</div>';
  h += '<div class="tgrid">';
  if (th.recognize && th.recognize.length){
    h += '<div class="card"><h4>How to recognise it</h4><ul>'+
         th.recognize.map(function(x){ return '<li>'+x+'</li>'; }).join('')+'</ul></div>';
  }
  if (th.pitfalls && th.pitfalls.length){
    h += '<div class="card"><h4>Where people go wrong</h4><ul>'+
         th.pitfalls.map(function(x){ return '<li>'+x+'</li>'; }).join('')+'</ul></div>';
  }
  h += '</div>';
  if (th.template){
    h += '<div class="sec"><h3>The reusable template</h3><pre class="tmpl">'+hl(th.template)+'</pre></div>';
  }
  if (th.variants && th.variants.length){
    h += '<div class="sec"><h3>If the interviewer twists it</h3><table class="var"><tr><th>Variant</th><th>What changes</th></tr>';
    th.variants.forEach(function(v){ h += '<tr><td>'+v[0]+'</td><td>'+v[1]+'</td></tr>'; });
    h += '</table></div>';
  }
  if (th.thinking){
    h += '<div class="sec"><h3>How to think about it next time</h3><div class="big">'+th.thinking+'</div></div>';
  }
  if (cx){
    h += '<div class="sec"><h3>Complexity</h3><div class="cx"><span><b>time</b> &nbsp;'+cx.time+
         '</span><span><b>space</b> &nbsp;'+cx.space+'</span>'+
         (cx.note?'<span style="color:var(--ink-3)">'+cx.note+'</span>':'')+'</div></div>';
  }
  h += '</div></div>';
  return h;
}

/* ------------------------------------------------------------
   6. main render
   ------------------------------------------------------------ */
LV.render = function (spec) {
  var T = spec.build();
  var i = 0, timer = null;
  var diff = (spec.difficulty||'').toLowerCase();

  document.title = spec.num + ' · ' + spec.name + ' — traced';

  var wrap = el('div','wrap');
  wrap.innerHTML =
    '<div class="mast">'+
      '<p class="crumb"><a href="./index.html">&#8592; all visualizations</a> &nbsp;·&nbsp; '+
        'RaghhavMalani / leetcode-progress</p>'+
      '<h1>'+spec.num+' &middot; '+esc(spec.name)+'</h1>'+
      '<div class="tagrow">'+
        '<span class="tag '+diff+'">'+esc(spec.difficulty||'')+'</span>'+
        '<span class="tag pat">'+esc(spec.pattern||'')+'</span>'+
        (spec.slug?'<span class="tag"><a href="../'+spec.slug+'/" target="_blank">solution folder</a></span>':'')+
        (spec.url?'<span class="tag"><a href="'+spec.url+'" target="_blank">leetcode</a></span>':'')+
      '</div>'+
      (spec.blurb?'<p style="margin:11px 0 0;color:var(--ink-2);max-width:80ch;font-size:13.5px">'+spec.blurb+'</p>':'')+
    '</div>'+

    '<div class="sec"><h3>Step through your own solution</h3>'+
    '<div class="title"><h2>'+esc(spec.runName||'trace')+'</h2><span class="inp">'+esc(spec.input||'')+'</span></div>'+
    '<div class="bar">'+
      '<button id="lv-reset">Reset</button>'+
      '<button id="lv-prev">&lsaquo; Back</button>'+
      '<button id="lv-play" class="primary">Play</button>'+
      '<button id="lv-next">Forward &rsaquo;</button>'+
      (spec.skipLabel!==null?'<button id="lv-skip">'+(spec.skipLabel||'Skip to next milestone')+'</button>':'')+
      '<span class="count" id="lv-count"></span>'+
    '</div>'+
    '<input class="scrub" id="lv-scrub" type="range" min="0" value="0" step="1" aria-label="step">'+
    '<div class="vars" id="lv-vars"></div>'+
    '<div class="grid2">'+
      '<div class="pane"><header>your code &mdash; '+esc(spec.slug||'')+'</header><div class="body" id="lv-code"></div></div>'+
      '<div class="pane"><header>state</header><div class="state" id="lv-state"></div></div>'+
    '</div>'+
    '<div class="msg" id="lv-msg"></div>'+
    '<div class="results" id="lv-res"></div>'+
    (spec.legend===false?'':'<div class="legend">'+
      '<span><i class="sw" style="background:#0d3a4e;border:1px solid var(--cy)"></i>active right now</span>'+
      '<span><i class="sw" style="background:#0b2c3d;border:1px solid #2a7ea0"></i>inside the window / region</span>'+
      '<span><i class="sw" style="background:#102a1e;border:1px solid var(--gr)"></i>settled / answer</span>'+
      '<span><i class="sw" style="background:#241318;border:1px solid #7a3b40"></i>discarded / dead end</span>'+
      '<span><i class="sw" style="background:#2a2110;border:1px solid #7a5a1e"></i>being undone</span>'+
      '</div>')+
    '</div>'+
    theoryHtml(spec.theory, spec.complexity)+
    '<div class="fnav">'+
      '<a href="./index.html">&#8592; all visualizations</a>'+
      '<a href="../PATTERNS.md">pattern handbook &#8594;</a>'+
    '</div>';
  document.body.appendChild(wrap);

  var codeEl  = document.getElementById('lv-code');
  var stateEl = document.getElementById('lv-state');
  var msgEl   = document.getElementById('lv-msg');
  var varsEl  = document.getElementById('lv-vars');
  var resEl   = document.getElementById('lv-res');
  var cntEl   = document.getElementById('lv-count');
  var scrub   = document.getElementById('lv-scrub');

  codeEl.innerHTML = spec.src.map(function (t,k){
    return '<div class="ln" data-l="'+(k+1)+'"><span class="no">'+(k+1)+'</span>'+hl(t)+'</div>';
  }).join('');
  var lnEls = codeEl.querySelectorAll('.ln');
  scrub.max = T.events.length-1;

  function flavour(t){
    if (t==='pop'||t==='undo') return 'pop';
    if (t==='found'||t==='done'||t==='ok') return 'good';
    if (t==='prune'||t==='bad'||t==='dup'||t==='skip2') return 'bad';
    return '';
  }

  function draw(){
    var e = T.events[i], fl = flavour(e.type);
    for (var k=0;k<lnEls.length;k++){
      var on = (+lnEls[k].dataset.l === e.line);
      lnEls[k].className = 'ln' + (on ? ' hi '+fl : '');
    }
    varsEl.innerHTML = e.vars.length ? e.vars.map(function(v){ return '<span>'+v+'</span>'; }).join('')
                                     : '<span style="color:var(--ink-4)">&mdash;</span>';
    varsEl.style.display = e.vars.length ? '' : 'none';
    stateEl.innerHTML = e.views.map(function(v){ return '<div class="view">'+drawView(v,i)+'</div>'; }).join('');
    msgEl.className = 'msg '+ (e.type==='done' ? 'good' : fl);
    msgEl.innerHTML = e.msg.replace(/`([^`]+)`/g, function(m,c){ return '<code>'+esc(c)+'</code>'; });
    resEl.innerHTML = e.out.length
      ? e.out.map(function(r){ return '<span class="slot">'+esc(r)+'</span>'; }).join('')
      : '<span class="slot pending">'+(spec.emptyResult||'nothing collected yet')+'</span>';
    resEl.style.display = (spec.showResults===false) ? 'none' : '';
    cntEl.textContent = 'step '+(i+1)+' of '+T.events.length;
    scrub.value = i;
    var hi = codeEl.querySelector('.ln.hi');
    if (hi && hi.scrollIntoView) hi.scrollIntoView({block:'nearest'});
    var ts = stateEl.querySelector('.treescroll');
    if (ts){
      var svg = ts.querySelector('svg'), cur = e.views.filter(function(v){return v.k==='tree';})[0];
      if (svg && cur && cur.tb.nodes[cur.cur]){
        var want = cur.tb.nodes[cur.cur].x - ts.clientWidth/2;
        ts.scrollLeft = Math.max(0, want);
      }
    }
  }
  function go(d){ i = Math.max(0, Math.min(T.events.length-1, i+d)); draw(); }
  function stop(){ if(timer){ clearInterval(timer); timer=null; document.getElementById('lv-play').textContent='Play'; } }

  document.getElementById('lv-next').onclick  = function(){ stop(); go(1); };
  document.getElementById('lv-prev').onclick  = function(){ stop(); go(-1); };
  document.getElementById('lv-reset').onclick = function(){ stop(); i=0; draw(); };
  var skipBtn = document.getElementById('lv-skip');
  if (skipBtn) skipBtn.onclick = function(){
    stop();
    var marks = spec.skipTypes || ['found','ok','done'];
    var j = i;
    do { j++; } while (j<T.events.length && marks.indexOf(T.events[j].type)<0);
    i = Math.min(j, T.events.length-1); draw();
  };
  document.getElementById('lv-play').onclick = function(){
    if (timer){ stop(); return; }
    if (i >= T.events.length-1) i = 0;
    this.textContent = 'Pause';
    timer = setInterval(function(){ if(i>=T.events.length-1){ stop(); return; } go(1); }, spec.speed||620);
  };
  scrub.oninput = function(){ stop(); i = +this.value; draw(); };
  document.addEventListener('keydown', function(ev){
    if (ev.target.tagName === 'INPUT' && ev.target.type === 'text') return;
    if (ev.key==='ArrowRight'){ stop(); go(1); ev.preventDefault(); }
    else if (ev.key==='ArrowLeft'){ stop(); go(-1); ev.preventDefault(); }
    else if (ev.key===' '){ document.getElementById('lv-play').click(); ev.preventDefault(); }
  });
  draw();
};

global.LV = LV;
})(window);
