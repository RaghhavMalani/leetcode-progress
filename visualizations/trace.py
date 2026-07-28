#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trace.py — generate a visualization page by ACTUALLY RUNNING a solution.

    python trace.py 0078-subsets
    python trace.py 0078-subsets --input "nums=[1,2,3,4]"
    python trace.py 0039-combination-sum --compare old.py     # before/after diff

Unlike the hand-authored pages, this reads nothing but the source file: it runs
the solution under sys.settrace, records the line number and every live local at
each step, and derives the narration from what actually changed. So the trace can
never drift from the code, and it works on any input you give it.

Input resolution, in order:
  1. --input "nums=[1,2,3]"
  2. cases.json in this folder, keyed by slug
  3. the first "Input:" line of the problem's README (LeetCode's own format)

Falls back cleanly: if a problem cannot be auto-run (design classes, missing
imports), it says so and leaves any existing hand-written page alone.
"""
import io, os, re, sys, json, html, argparse, ast, inspect
from collections import defaultdict, deque, Counter
import heapq, math, itertools, functools, bisect, string

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
MAX_EVENTS = 420          # a page past this is unreadable; we sample instead

# ----------------------------------------------------------------- helpers
INDEXY = {'i','j','k','l','r','x','y','lo','hi','mid','left','right','start','end',
          'low','high','slow','fast','curr','cur','idx','index','pos','p','q','head','tail'}

def repo_file(slug, ext='py'):
    d = os.path.join(REPO, slug)
    if not os.path.isdir(d): return None
    for f in sorted(os.listdir(d)):
        if f.endswith('.'+ext): return os.path.join(d, f)
    return None

def read_lines(path):
    return io.open(path, encoding='utf-8').read().replace('\t','    ').rstrip().split('\n')

# ----------------------------------------------------------------- input parsing
def parse_kwargs(expr):
    """'nums = [2,7,11,15], target = 9'  ->  {'nums':[2,7,11,15],'target':9}"""
    expr = expr.strip().rstrip(',')
    if not expr: return {}
    # split on commas that are not inside brackets/quotes
    parts, depth, buf, quote = [], 0, '', None
    for ch in expr:
        if quote:
            buf += ch
            if ch == quote: quote = None
            continue
        if ch in '"\'': quote = ch; buf += ch; continue
        if ch in '[({': depth += 1
        elif ch in '])}': depth -= 1
        if ch == ',' and depth == 0: parts.append(buf); buf = ''
        else: buf += ch
    if buf.strip(): parts.append(buf)
    out = {}
    for p in parts:
        if '=' not in p: continue
        k, v = p.split('=', 1)
        k = k.strip()
        if not re.match(r'^[A-Za-z_]\w*$', k): continue
        v = v.strip()
        v = re.sub(r'\bnull\b','None',v); v = re.sub(r'\btrue\b','True',v); v = re.sub(r'\bfalse\b','False',v)
        try: out[k] = ast.literal_eval(v)
        except Exception: return {}          # give up on the whole thing, not just one arg
    return out

def input_from_readme(slug):
    p = os.path.join(REPO, slug, 'README.md')
    if not os.path.exists(p): return {}
    txt = io.open(p, encoding='utf-8').read()
    txt = re.sub(r'<[^>]+>', '', html.unescape(txt)).replace('\xa0',' ')
    m = re.search(r'Input:\s*([\s\S]*?)(?:\n\s*(?:Output|Explanation)\s*:|\Z)', txt)
    if not m: return {}
    raw = re.sub(r'\s*\n\s*', ' ', m.group(1)).strip()
    kw = parse_kwargs(raw)
    if kw: return kw
    return parse_kwargs(raw.split('\n')[0])

def resolve_input(slug, cli):
    if cli:
        kw = parse_kwargs(cli)
        if kw: return kw, 'the input you gave'
    cases = {}
    cp = os.path.join(ROOT, 'cases.json')
    if os.path.exists(cp):
        try: cases = json.load(io.open(cp, encoding='utf-8'))
        except Exception: pass
    if slug in cases:
        kw = parse_kwargs(cases[slug]) if isinstance(cases[slug], str) else cases[slug]
        if kw: return kw, 'cases.json'
    kw = input_from_readme(slug)
    if kw: return kw, "the README's first example"
    return {}, None

# ----------------------------------------------------------------- running
import typing
SAFE_GLOBALS = dict(
    List=typing.List, Optional=typing.Optional, Dict=typing.Dict,
    Tuple=typing.Tuple, Set=typing.Set, Any=typing.Any, typing=typing,
    defaultdict=defaultdict, deque=deque, Counter=Counter, heapq=heapq,
    math=math, itertools=itertools, functools=functools, bisect=bisect,
    string=string, lru_cache=functools.lru_cache, cache=functools.lru_cache(None),
)
try:
    import collections
    SAFE_GLOBALS['collections'] = collections
except Exception: pass

class ListNode:
    def __init__(self, val=0, next=None): self.val, self.next = val, next
    def __repr__(self):
        out, n, g = [], self, 0
        while n and g < 40: out.append(str(n.val)); n = n.next; g += 1
        return ' -> '.join(out) if out else 'None'
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
    def __repr__(self): return 'TreeNode(%r)' % self.val
SAFE_GLOBALS['ListNode'] = ListNode
SAFE_GLOBALS['TreeNode'] = TreeNode

LIST_PARAMS = {'head','l1','l2','list1','list2','node','lists'}
TREE_PARAMS = {'root'}

def build_list(a):
    d = ListNode(); t = d
    for x in (a or []): t.next = ListNode(x); t = t.next
    return d.next

def build_tree(a):
    if not a: return None
    nodes = [None if x is None else TreeNode(x) for x in a]
    kids = deque(nodes[1:])
    for n in nodes:
        if n is None: continue
        if kids: n.left = kids.popleft()
        if kids: n.right = kids.popleft()
    return nodes[0]

def coerce(params, kwargs):
    """Turn README arrays into the objects the signature actually wants."""
    out = dict(kwargs)
    for p in params:
        if p not in out: continue
        v = out[p]
        if p in LIST_PARAMS and isinstance(v, list):
            out[p] = [build_list(x) for x in v] if p == 'lists' else build_list(v)
        elif p in TREE_PARAMS and isinstance(v, list):
            out[p] = build_tree(v)
    return out

def load_solution(path):
    src = io.open(path, encoding='utf-8').read()
    g = dict(SAFE_GLOBALS); g['__name__'] = '__trace__'
    code = compile(src, path, 'exec')
    exec(code, g)
    return g, src

def pick_entry(g, kwargs):
    """Find Solution().<method> whose parameters best match the given kwargs."""
    cls = g.get('Solution')
    if cls is None: return None, None
    meths = [(n, f) for n, f in vars(cls).items()
             if callable(f) and not n.startswith('_')]
    if not meths: return None, None
    def score(item):
        n, f = item
        try: params = [p for p in inspect.signature(f).parameters if p != 'self']
        except Exception: params = []
        return (len(set(params) & set(kwargs)), -abs(len(params) - len(kwargs)))
    meths.sort(key=score, reverse=True)
    name, fn = meths[0]
    try: params = [p for p in inspect.signature(fn).parameters if p != 'self']
    except Exception: params = []
    return (cls, name), params

def snap(v, budget=64):
    """A JSON-safe, size-capped snapshot of a local."""
    try:
        if v is None or isinstance(v, (bool, int, float, str)):
            return v if not isinstance(v, str) or len(v) <= 120 else v[:120]+'…'
        if isinstance(v, (list, tuple)):
            if len(v) > budget: return [snap(x, 8) for x in v[:budget]] + ['…']
            return [snap(x, 8) for x in v]
        if isinstance(v, set):
            xs = sorted(v, key=lambda z: str(z))[:budget]
            return {'__set__': [snap(x, 8) for x in xs]}
        if isinstance(v, dict):
            items = list(v.items())[:budget]
            return {'__dict__': [[snap(k, 8), snap(x, 8)] for k, x in items]}
        return '<'+type(v).__name__+'>'
    except Exception:
        return '<?>'

def run_traced(path, kwargs):
    g, src = load_solution(path)
    entry, params = pick_entry(g, kwargs)
    if entry is None:
        raise RuntimeError('no Solution class with a public method — '
                           'design-style problems need a hand-written trace')
    cls, meth = entry
    kwargs = coerce(params, kwargs)
    if all(p in kwargs for p in params):
        args = [kwargs[p] for p in params]
    elif len(kwargs) == len(params):
        # README uses different names (e.g. 'candidates' vs 'nums') - map in order
        vals = list(kwargs.values())
        kwargs = dict(zip(params, vals))
        kwargs = coerce(params, kwargs)
        args = [kwargs[p] for p in params]
    else:
        raise RuntimeError('input does not match %s(%s); got %s'
                           % (meth, ', '.join(params), ', '.join(sorted(kwargs))))
    obj = cls()
    events = []
    fname = path
    def tracer(frame, event, arg):
        if frame.f_code.co_filename != fname: return None
        if event == 'line' and len(events) < MAX_EVENTS*4:
            loc = {}
            for k, v in frame.f_locals.items():
                if k in ('self',) or k.startswith('__'): continue
                if callable(v): continue
                loc[k] = snap(v)
            events.append({'line': frame.f_lineno, 'fn': frame.f_code.co_name, 'loc': loc})
        return tracer
    sys.settrace(tracer)
    try:
        result = getattr(obj, meth)(*[x for x in args])
    finally:
        sys.settrace(None)
    return events, result, src, meth, params, kwargs

# ----------------------------------------------------------------- narration
def describe(prev, cur):
    """Plain-English diff of two locals dicts."""
    bits = []
    for k in cur:
        a, b = prev.get(k, '__none__'), cur[k]
        if a == b: continue
        if a == '__none__':
            bits.append('<b>%s</b> = %s' % (k, fmt(b)))
        elif isinstance(b, list) and isinstance(a, list):
            if len(b) == len(a)+1: bits.append('<b>%s</b> grows to %s' % (k, fmt(b)))
            elif len(b) == len(a)-1: bits.append('<b>%s</b> shrinks to %s' % (k, fmt(b)))
            else: bits.append('<b>%s</b> becomes %s' % (k, fmt(b)))
        elif isinstance(b, (int, float)) and isinstance(a, (int, float)):
            d = b - a
            bits.append('<b>%s</b> %s to %s' % (k, ('rises' if d > 0 else 'falls'), fmt(b)))
        else:
            bits.append('<b>%s</b> becomes %s' % (k, fmt(b)))
    if not bits: return 'The line runs; no tracked value changes.'
    return ' &middot; '.join(bits[:4]) + ('' if len(bits) <= 4 else ' &middot; …')

def fmt(v):
    if isinstance(v, dict) and '__dict__' in v:
        return '{' + ', '.join('%s: %s' % (fmt(k), fmt(x)) for k, x in v['__dict__'][:6]) + '}'
    if isinstance(v, dict) and '__set__' in v:
        return '{' + ', '.join(fmt(x) for x in v['__set__'][:8]) + '}'
    if isinstance(v, list): return '[' + ', '.join(fmt(x) for x in v[:10]) + ']'
    if isinstance(v, str):  return '"%s"' % v
    return str(v)

def classify(prev, cur, line, src_line):
    """Guess an event type so the quiz options and colours still work."""
    s = (src_line or '').strip()
    for k in cur:
        a, b = prev.get(k), cur[k]
        if isinstance(b, list) and isinstance(a, list):
            if len(b) > len(a): return 'push'
            if len(b) < len(a): return 'pop'
    if s.startswith('return'): return 'ok'
    if re.match(r'^(if|elif|while)\b', s): return 'call'
    if '.append' in s or '.push' in s or '.add' in s: return 'push'
    if '.pop' in s or 'del ' in s or '.remove' in s: return 'pop'
    return 'info'

# ----------------------------------------------------------------- views
def view_js(name, v, marks_from):
    """Emit a JS expression for one local, chosen by its Python type."""
    j = json.dumps
    if isinstance(v, dict) and '__dict__' in v:
        pairs = [[fmt_plain(k), fmt_plain(x)] for k, x in v['__dict__']]
        return 'LV.kv(%s,%s,{},{emptyText:"empty"})' % (j(name), j(pairs))
    if isinstance(v, dict) and '__set__' in v:
        return 'LV.kv(%s,%s,{},{emptyText:"empty"})' % (j(name), j([fmt_plain(x) for x in v['__set__']]))
    if isinstance(v, list):
        if v and all(isinstance(x, list) for x in v):
            rows = [[fmt_plain(y) for y in row] for row in v]
            return 'LV.grid(%s,%s,{},{head:true})' % (j(name), j(rows))
        marks = {}
        for mk, mv in marks_from.items():
            if isinstance(mv, int) and not isinstance(mv, bool) and 0 <= mv < len(v):
                marks[str(mv)] = 'hot'
        return 'LV.arr(%s,%s,%s,{ptrs:%s})' % (
            j(name), j([fmt_plain(x) for x in v]), j(marks),
            j({str(mv): mk for mk, mv in marks_from.items()
               if isinstance(mv, int) and not isinstance(mv, bool) and 0 <= mv < len(v)}))
    if isinstance(v, str) and len(v) <= 60:
        return 'LV.arr(%s,%s,{},{})' % (j(name), j(list(v)))
    return None

def fmt_plain(v):
    if isinstance(v, dict) and '__dict__' in v: return fmt(v)
    if isinstance(v, dict) and '__set__' in v: return fmt(v)
    if isinstance(v, list): return fmt(v)
    return v if isinstance(v, (int, float, str)) else str(v)

# ----------------------------------------------------------------- page
PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="%(base)s_engine.css">
</head>
<body>
<script src="%(base)s_engine.js"></script>
<script>
var SRC = %(src)s;
function build(){
  var T = LV.trace();
%(steps)s
  return T;
}
LV.render({
  num:%(num)s, name:%(name)s, slug:%(slug)s,
  difficulty:%(diff)s, pattern:'Auto-traced from real execution',
  url:%(url)s,
  blurb:'This page was generated by running the solution under <code>sys.settrace</code> and recording what actually happened \\u2014 every line, every live variable. It can never drift from the code.',
  input:%(input)s, runName:%(run)s,
  skipLabel:null, emptyResult:'nothing recorded',
  showResults:false,
  src: SRC, build: build,
  complexity:{time:'\\u2014 (measure it yourself; this page only shows behaviour)', space:'\\u2014'},
  theory:{
    idea:'%(idea)s',
    recognize:['This trace was generated automatically, so there is no hand-written theory for it yet.',
               'Open <a href="index.html">the index</a> to find the pattern family it belongs to, then read that family in <a href="../PATTERNS.md">PATTERNS.md</a>.'],
    pitfalls:['Auto-traces show <b>what</b> happened, not <b>why</b>. Watch it once, then write your own one-sentence explanation of the invariant \\u2014 that is the part that makes it stick.'],
    thinking:'Re-run this on a different input with <code>python trace.py %(slugplain)s --input "..."</code>. Watching the same code on an edge case \\u2014 an empty list, all-equal values, a single element \\u2014 is the fastest way to find out whether you actually understand it.'
  }
});
</script>
</body>
</html>
"""

def build_page(slug, events, result, src, meth, kwargs, source_note, out_path, base='./'):
    lines = src.split('\n')
    # collapse consecutive identical (line, locals) and cap the length
    trimmed = []
    for e in events:
        if trimmed and trimmed[-1]['line'] == e['line'] and trimmed[-1]['loc'] == e['loc']:
            continue
        trimmed.append(e)
    if len(trimmed) > MAX_EVENTS:
        stride = len(trimmed) / float(MAX_EVENTS)
        trimmed = [trimmed[int(i*stride)] for i in range(MAX_EVENTS)]
    steps, prev = [], {}
    for e in trimmed:
        src_line = lines[e['line']-1] if 0 < e['line'] <= len(lines) else ''
        typ = classify(prev, e['loc'], e['line'], src_line)
        msg = describe(prev, e['loc'])
        scal = {k: v for k, v in e['loc'].items()
                if isinstance(v, (int, float, bool)) or (isinstance(v, str) and len(v) < 24)}
        vars_js = json.dumps(['%s = <b>%s</b>' % (k, html.escape(str(fmt(v)))) for k, v in sorted(scal.items())][:6])
        views = []
        for k, v in sorted(e['loc'].items()):
            if isinstance(v, (int, float, bool)) or v is None: continue
            if isinstance(v, str) and len(v) < 24: continue
            js = view_js(k, v, {kk: vv for kk, vv in scal.items() if kk in INDEXY})
            if js: views.append(js)
        steps.append('  T.step(%d,%s,%s,%s,[%s]);'
                     % (e['line'], json.dumps(typ), json.dumps(msg), vars_js, ','.join(views[:4])))
        prev = e['loc']                      # <- describe the DELTA, not the world
    steps.append('  T.step(%d,"done",%s,[],[]);'
                 % (trimmed[-1]['line'] if trimmed else 1,
                    json.dumps('Finished. <b>%s</b> returned %s' % (meth, html.escape(fmt(snap(result)))))))

    num = str(int(slug.split('-')[0]))
    name = ' '.join(w.capitalize() for w in slug.split('-')[1:])
    rd = os.path.join(REPO, slug, 'README.md')
    diff, url = 'Unrated', ''
    if os.path.exists(rd):
        t = io.open(rd, encoding='utf-8').read()
        m = re.match(r'<h2><a href="([^"]+)">([^<]+)</a></h2><h3>(\w+)</h3>', t)
        if m:
            url, diff = m.group(1), m.group(3)
            name = re.sub(r'^\d+\.\s*', '', m.group(2))
    inp = ', '.join('%s = %s' % (k, fmt(snap(v))) for k, v in kwargs.items())
    page = PAGE % dict(
        title=html.escape('%s. %s — auto-traced' % (num, name)),
        base=base, src=json.dumps(lines, ensure_ascii=False),
        steps='\n'.join(steps), num=json.dumps(num), name=json.dumps(name),
        slug=json.dumps(slug), diff=json.dumps(diff), url=json.dumps(url),
        input=json.dumps(inp), run=json.dumps(meth+'()'),
        slugplain=slug,
        idea='Generated by real execution, using <b>%s</b>. %d recorded steps.'
             % (html.escape(source_note or 'a default input'), len(trimmed)))
    io.open(out_path, 'w', encoding='utf-8').write(page)
    return len(trimmed)

# ----------------------------------------------------------------- cli
def trace_one(slug, cli_input=None, out=None, quiet=False):
    path = repo_file(slug, 'py')
    if not path:
        if not quiet: print('  skip %-58s no .py solution' % slug)
        return None
    kwargs, note = resolve_input(slug, cli_input)
    if not kwargs:
        if not quiet: print('  skip %-58s could not work out an input' % slug)
        return None
    try:
        events, result, src, meth, params, kwargs = run_traced(path, kwargs)
    except Exception as e:
        if not quiet: print('  skip %-58s %s' % (slug, str(e)[:70]))
        return None
    if not events:
        if not quiet: print('  skip %-58s no lines executed' % slug);
        return None
    out = out or os.path.join(ROOT, slug + '.auto.html')
    n = build_page(slug, events, result, src, meth, kwargs, note, out)
    if not quiet: print('  ok   %-58s %3d steps -> %s' % (slug, n, os.path.basename(out)))
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug', nargs='?', help='problem folder name, or "all"')
    ap.add_argument('--input', help='e.g. "nums=[1,2,3], target=4"')
    ap.add_argument('--out', help='output html path')
    ap.add_argument('--missing', action='store_true',
                    help='trace every problem that has no hand-written page yet')
    a = ap.parse_args()

    if a.missing or a.slug == 'all':
        done = 0
        for d in sorted(os.listdir(REPO)):
            if not re.match(r'^\d{4}-', d): continue
            if a.missing and os.path.exists(os.path.join(ROOT, d + '.html')): continue
            if trace_one(d): done += 1
        print('\n%d page%s generated.' % (done, '' if done == 1 else 's'))
        return
    if not a.slug:
        ap.print_help(); return
    trace_one(a.slug, a.input, a.out)

if __name__ == '__main__':
    main()
