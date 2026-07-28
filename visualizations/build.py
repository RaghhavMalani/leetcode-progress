#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — regenerate every derived artifact from what is actually in the repo.

    python build.py            # rebuild everything
    python build.py --new      # only touch problems that have no page yet

Produces:
  <slug>.html                 traced page  (hand-written kept; new ones auto-traced)
  ../<slug>/visualization.html  the same page, viewable from the problem folder
  ../<slug>/NOTES.md          theory scoped to that problem
  index.html                  the browsable index, grouped by family
  dojo-data.js                the Dojo's dataset
  _index.json / _groups.json  metadata other tools read

Safe to run any time: hand-written pages are never overwritten.
"""
import io, os, re, sys, json, html, glob, subprocess, argparse, random
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
sys.path.insert(0, ROOT)

# ---------------------------------------------------------------- families
FAMILIES = [
 ("Backtracking", "Choose → explore → un-choose. One shared mutable path, mutated on the way down and rewound on the way up."),
 ("Two pointers & sliding window", "Two indices that only ever move forward, so an inner while loop is still linear overall."),
 ("Hashing", "Trade memory for O(1) lookup: complement lookup, canonical keys, frequency counts."),
 ("Linked lists", "No random access, so every problem is about not losing your grip on a node."),
 ("Stacks & monotonic stacks", "A stack is a queue of unanswered questions, kept sorted so one fact resolves many."),
 ("Binary search", "Maintain an invariant while halving a range — including halving the ANSWER."),
 ("Trees", "Decide what a node returns to its parent versus what it contributes to the answer."),
 ("Graphs, BFS & DFS", "Minimum steps means BFS. Connectivity means DFS or union-find. Weighted means Dijkstra."),
 ("Dynamic programming", "State, recurrence, base cases, fill order — then ask how far back the recurrence reaches."),
 ("Greedy", "A greedy you cannot justify is a greedy you will misapply. Pair it with an exchange argument."),
 ("Prefix sums & intervals", "Precompute so queries are cheap; for intervals, the sort key is the algorithm."),
 ("Bit manipulation", "XOR cancels pairs, AND only clears bits, OR only sets them. That monotonicity is the algorithm."),
 ("Math & number theory", "Euclid, modular arithmetic, base conversion, index arithmetic, closed forms."),
 ("Design", "Compose structures: one per required operation, cross-referenced."),
 ("Sorting & divide and conquer", "T(n) = 2T(n/2) + O(n). Draw the recursion tree once and you own the argument."),
 ("Brute force done right", "Sometimes O(n²) is intended. Make the inner step O(1) and name the next rung."),
]
FAM_NAMES = [f[0] for f in FAMILIES]
FAM_DESC  = {f[0]: f[1] for f in FAMILIES}

# LeetHub topic tag  ->  family
TOPIC_FAM = {
 'backtracking':'Backtracking','recursion':'Backtracking',
 'two pointers':'Two pointers & sliding window','sliding window':'Two pointers & sliding window',
 'hash table':'Hashing','counting':'Hashing','bucket sort':'Hashing','hash function':'Hashing',
 'linked list':'Linked lists',
 'stack':'Stacks & monotonic stacks','monotonic stack':'Stacks & monotonic stacks','queue':'Stacks & monotonic stacks',
 'binary search':'Binary search',
 'tree':'Trees','binary tree':'Trees','binary search tree':'Trees','depth-first search':'Graphs, BFS & DFS',
 'breadth-first search':'Graphs, BFS & DFS','graph':'Graphs, BFS & DFS','union find':'Graphs, BFS & DFS',
 'topological sort':'Graphs, BFS & DFS','shortest path':'Graphs, BFS & DFS','matrix':'Graphs, BFS & DFS',
 'dynamic programming':'Dynamic programming','memoization':'Dynamic programming','probability and statistics':'Dynamic programming',
 'greedy':'Greedy',
 'prefix sum':'Prefix sums & intervals','interval':'Prefix sums & intervals','line sweep':'Prefix sums & intervals',
 'binary indexed tree':'Prefix sums & intervals','segment tree':'Prefix sums & intervals','merge sort':'Sorting & divide and conquer',
 'bit manipulation':'Bit manipulation','bitmask':'Bit manipulation',
 'math':'Math & number theory','number theory':'Math & number theory','simulation':'Math & number theory',
 'design':'Design','heap (priority queue)':'Design','ordered set':'Design',
 'sorting':'Sorting & divide and conquer','divide and conquer':'Sorting & divide and conquer','quickselect':'Sorting & divide and conquer',
 'enumeration':'Brute force done right','brainteaser':'Brute force done right',
 'string':'Hashing','array':'Two pointers & sliding window','string matching':'Brute force done right',
}
# source-code fingerprints, used when no topic tag exists
SRC_FAM = [
 # choose / explore / un-choose in the code beats any wording in the statement
 (r'(?s)(?:def\s+(?:dfs|backtrack|bt|helper)\b)[\s\S]{0,900}?\.pop\(\)', 'Backtracking', 10),
 (r'(?s)\.append\([^\n]*\)[\s\S]{0,400}?\.pop\(\)[\s\S]{0,60}$',      'Backtracking', 8),
 (r'\.pop\(\)\s*$|\.pop\(\)\n',                 'Backtracking',   2),
 (r'heapq|heappush|priority',                    'Design',         3),
 (r'deque\(|popleft',                            'Graphs, BFS & DFS', 4),
 (r'\bdp\b|memo|lru_cache',                      'Dynamic programming', 4),
 (r'while\s+\w*left\w*\s*<=?\s*\w*right|bisect', 'Binary search',  3),
 (r'stack\s*=\s*\[\]',                           'Stacks & monotonic stacks', 3),
 (r'\.next\b|ListNode',                          'Linked lists',   4),
 (r'TreeNode|root\.left',                        'Trees',          4),
 (r'\^|<<|>>|\&\s*1',                            'Bit manipulation', 2),
 (r'prefix|postfix|suffix',                      'Prefix sums & intervals', 2),
 (r'\.sort\(|sorted\(',                          'Greedy',         1),
 (r'defaultdict|Counter|\{\}',                   'Hashing',        1),
]

def leethub_topics():
    """slug -> [topic, ...] from the table LeetHub maintains in the root README."""
    p = os.path.join(REPO, 'README.md')
    if not os.path.exists(p): return {}
    t = io.open(p, encoding='utf-8').read()
    parts = re.split(r'\n#\s*LeetCode Topics\s*\n', t)
    if len(parts) < 2: return {}
    out = {}
    for name, block in re.findall(r'\n##\s*([^\n]+)\n((?:\|[^\n]*\n)+)', parts[1]):
        for slug in re.findall(r'\[([^\]]+)\]', block):
            out.setdefault(slug.strip(), []).append(name.strip().lower())
    return out

# the problem statement is the strongest signal of all
PROMPT_FAM = [
 (r'\ball (?:the )?(?:possible )?(?:combinations|permutations|subsets|ways to arrange)', 'Backtracking', 9),
 (r'\bsubarray\b|\bsubstring\b|\bcontiguous\b',      'Two pointers & sliding window', 6),
 (r'\bhow many ways\b|\bnumber of ways\b|\bminimum cost\b|\bmaximum (?:sum|profit|value)\b', 'Dynamic programming', 6),
 (r'\blinked list\b|\bListNode\b',                     'Linked lists', 9),
 (r'\bbinary tree\b|\bbinary search tree\b|\broot of\b','Trees', 9),
 (r'\bgraph\b|\bnodes? and edges\b|\bconnected\b|\bgrid\b|\bislands?\b', 'Graphs, BFS & DFS', 7),
 (r'\bsorted array\b.*\bO\(log n\)|\bO\(log n\) runtime', 'Binary search', 8),
 (r'\bdesign\b|\bimplement the\b.*\bclass\b',        'Design', 9),
 (r'\bintervals?\b',                                    'Prefix sums & intervals', 7),
 (r'\bbitwise\b|\bXOR\b|\bbits?\b',                  'Bit manipulation', 7),
 (r'\bnext greater\b|\bvalid parenthes|\bstack\b',    'Stacks & monotonic stacks', 7),
 (r'\banagram\b|\bfrequency\b|\bduplicate\b|\bcount of\b', 'Hashing', 5),
]

# LeetCode tags most problems with several topics. Prefer the most specific:
# "backtracking" tells you far more than "array" or "string".
TOPIC_RANK = {'backtracking':10,'dynamic programming':10,'binary search':9,'sliding window':9,
 'monotonic stack':9,'union find':9,'topological sort':9,'binary indexed tree':9,'segment tree':9,
 'divide and conquer':8,'two pointers':8,'linked list':8,'trie':8,'design':8,'bit manipulation':8,
 'heap (priority queue)':8,'breadth-first search':7,'depth-first search':7,'graph':7,'tree':7,
 'binary tree':7,'binary search tree':7,'prefix sum':7,'greedy':7,'stack':6,'queue':6,'interval':6,
 'line sweep':6,'quickselect':6,'memoization':6,'bucket sort':5,'counting':4,'sorting':4,
 'hash table':4,'matrix':3,'math':3,'simulation':3,'enumeration':2,'string':2,'array':1}

def classify(slug, topics, src, prompt=''):
    tags = [t for t in topics.get(slug, []) if t in TOPIC_FAM]
    if tags:
        best = max(tags, key=lambda t: TOPIC_RANK.get(t, 5))
        return TOPIC_FAM[best], 'topic tag "%s"' % best
    best, score, why = 'Math & number theory', 0, 'fallback'
    for pat, fam, w in PROMPT_FAM:
        if re.search(pat, prompt, re.I) and w > score:
            best, score, why = fam, w, 'statement wording'
    for pat, fam, w in SRC_FAM:
        if re.search(pat, src, re.M) and w > score:
            best, score, why = fam, w, 'source pattern'
    return best, why

# ---------------------------------------------------------------- scanning
def sol_file(slug):
    d = os.path.join(REPO, slug)
    for ext in ('py','cpp','java','c'):
        for f in sorted(glob.glob(os.path.join(d, '*.'+ext))):
            return f
    return None

def readme_meta(slug):
    p = os.path.join(REPO, slug, 'README.md')
    if not os.path.exists(p): return {}
    t = io.open(p, encoding='utf-8').read()
    m = re.match(r'<h2><a href="([^"]+)">([^<]+)</a></h2><h3>(\w+)</h3><hr>([\s\S]*)', t)
    if not m: return {}
    body = re.sub(r'</?(p|div|li|ul|ol|pre|h\d)[^>]*>', '\n', m.group(4))
    body = re.sub(r'<br\s*/?>', '\n', body); body = re.sub(r'<[^>]+>', '', body)
    body = html.unescape(body).replace('\xa0', ' ')
    body = re.sub(r'[ \t]+', ' ', re.sub(r'\n{3,}', '\n\n', body)).strip()
    prompt = re.split(r'\n\s*Example\s*1?\s*:', body, maxsplit=1)[0].strip()
    cons = ''
    cm = re.search(r'Constraints:\s*([\s\S]*?)(?:\n\s*Follow[- ]up|$)', body, re.I)
    if cm: cons = re.sub(r'\n+', '\n', cm.group(1)).strip()[:400]
    ex = ''
    em = re.search(r'(Input:[\s\S]{0,260})', body)
    if em: ex = em.group(1).strip()
    return {'url': m.group(1), 'title': re.sub(r'^\d+\.\s*', '', m.group(2)),
            'difficulty': m.group(3), 'prompt': prompt[:900], 'constraints': cons, 'example': ex}

def page_field(page, name):
    if not os.path.exists(page): return ''
    s = io.open(page, encoding='utf-8').read()
    m = re.search(name + r":\s*'((?:[^'\\]|\\.)*)'", s)
    return m.group(1).replace("\\'", "'") if m else ''

def scan():
    topics = leethub_topics()
    out = []
    for d in sorted(os.listdir(REPO)):
        if not re.match(r'^\d{4}-', d) or not os.path.isdir(os.path.join(REPO, d)): continue
        sf = sol_file(d)
        meta = readme_meta(d)
        page = os.path.join(ROOT, d + '.html')
        auto = os.path.join(ROOT, d + '.auto.html')
        has = os.path.exists(page)
        src = io.open(sf, encoding='utf-8').read() if sf else ''
        fam = page_field(page, 'pattern') and None
        family, why = classify(d, topics, src, meta.get('prompt',''))
        # a hand-written page's family (from _groups.json) wins if we have it
        rec = {'slug': d, 'num': int(d.split('-')[0]), 'name': meta.get('title') or
               ' '.join(w.capitalize() for w in d.split('-')[1:]),
               'difficulty': meta.get('difficulty', ''), 'url': meta.get('url', ''),
               'prompt': meta.get('prompt', ''), 'constraints': meta.get('constraints', ''),
               'example': meta.get('example', ''), 'solved': bool(sf), 'solfile': sf,
               'page': page if has else (auto if os.path.exists(auto) else None),
               'handwritten': has, 'family': family, 'why': why,
               'pattern': page_field(page, 'pattern') or ('Auto-traced · ' + family)}
        out.append(rec)
    # keep the families already assigned to hand-written pages
    gp = os.path.join(ROOT, '_groups.json')
    if os.path.exists(gp):
        try:
            old = json.load(io.open(gp, encoding='utf-8'))
            known = {}
            for f, rows in old['groups'].items():
                for r in rows: known[r['slug']] = f
            for r in out:
                if r['handwritten'] and r['slug'] in known: r['family'] = known[r['slug']]
        except Exception: pass
    return out

# ---------------------------------------------------------------- outputs
def write_index(recs):
    groups = {}
    for r in recs:
        if not r['page']: continue
        groups.setdefault(r['family'], []).append(r)
    for g in groups: groups[g].sort(key=lambda r: r['num'])
    cards = []
    for fam in FAM_NAMES:
        rows = groups.get(fam, [])
        if not rows: continue
        cards.append('<div class="patsec"><h3>%s <span>%d problem%s</span></h3><p>%s</p><div class="cardgrid">%s</div></div>' % (
            html.escape(fam), len(rows), '' if len(rows) == 1 else 's', html.escape(FAM_DESC[fam]),
            ''.join('<a class="pcard" href="./%s" data-t="%s"><div class="n">%s%s</div><div class="t">%s</div>'
                    '<div class="d %s">%s</div></a>' % (
                     os.path.basename(r['page']),
                     html.escape((str(r['num'])+' '+r['name']+' '+r['pattern']+' '+fam).lower()),
                     r['num'], '' if r['handwritten'] else ' &middot; auto',
                     html.escape(r['name']), r['difficulty'].lower(), r['difficulty'])
                    for r in rows)))
    n = sum(len(v) for v in groups.values())
    tmpl = io.open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT,'index.html')) else ''
    body = '<div id="list">%s</div>' % ''.join(cards)
    if tmpl and '<div id="list">' in tmpl:
        out = re.sub(r'<div id="list">[\s\S]*?</div>\s*(?=<div class="fnav")', body + '\n  ', tmpl)
        out = re.sub(r'>\d+ problems from this repo', '>%d problems from this repo' % n, out)
        out = re.sub(r'all \d+ traced solutions', 'all %d traced solutions' % n, out)
    else:
        out = body
    io.open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
    # metadata for other tools
    json.dump([{k: r[k] for k in ('slug','num','name','difficulty','pattern','family','url')} for r in recs if r['page']],
              io.open(os.path.join(ROOT, '_index.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump({'families': FAM_NAMES, 'desc': FAM_DESC,
               'groups': {f: [{k: r[k] for k in ('slug','num','name','difficulty','pattern')} for r in rows]
                          for f, rows in groups.items()}},
              io.open(os.path.join(ROOT, '_groups.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return n

def write_folder_pages(recs):
    """A viewable copy of each page inside its own problem folder."""
    n = 0
    for r in recs:
        if not r['page']: continue
        s = io.open(r['page'], encoding='utf-8').read()
        for a, c in (('href="_engine.css"',   'href="../visualizations/_engine.css"'),
                     ('href="./_engine.css"', 'href="../visualizations/_engine.css"'),
                     ('src="_engine.js"',     'src="../visualizations/_engine.js"'),
                     ('src="./_engine.js"',   'src="../visualizations/_engine.js"'),
                     ('href="index.html"',    'href="../visualizations/index.html"')):
            s = s.replace(a, c)
        s = s.replace('href="./index.html"', 'href="../visualizations/index.html"')
        s = s.replace("href=\"./'+spec.slug+'.html\"", "href=\"../visualizations/'+spec.slug+'.html\"")
        s = s.replace('href="../PATTERNS.md"', 'href="../PATTERNS.md"')
        s = s.replace("'../'+spec.slug+'/'", "'./'")
        io.open(os.path.join(REPO, r['slug'], 'visualization.html'), 'w', encoding='utf-8').write(s)
        n += 1
    return n

def write_notes(recs, only_new=False):
    import _check
    eng = io.open(os.path.join(ROOT, '_engine.js'), encoding='utf-8').read()
    def md(s):
        s = re.sub(r'<code>(.*?)</code>', r'`\1`', s, flags=re.S)
        s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.S)
        s = re.sub(r'<em>(.*?)</em>', r'*\1*', s, flags=re.S)
        return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
    n = 0
    for r in recs:
        note = os.path.join(REPO, r['slug'], 'NOTES.md')
        if only_new and os.path.exists(note): continue
        if not r['page']:
            io.open(note, 'w', encoding='utf-8').write(
                '# %d. %s\n> **%s** &nbsp;&middot;&nbsp; **not solved yet**\n\n'
                'No solution file in this folder yet, so there is nothing to trace.\n\n'
                '---\n\n[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; '
                '[pattern handbook](../PATTERNS.md)\n' % (r['num'], r['name'], r['difficulty'] or 'Unrated'))
            n += 1; continue
        body = '\n'.join(re.findall(r'<script>([\s\S]*?)</script>', io.open(r['page'], encoding='utf-8').read()))
        h = _check.STUB + eng + "\nvar __spec=null;LV.render=function(s){__spec=s;};\n" + body + """
var T=__spec.build();
console.log(JSON.stringify({num:__spec.num,name:__spec.name,slug:__spec.slug,difficulty:__spec.difficulty,
 pattern:__spec.pattern,url:__spec.url,blurb:__spec.blurb,input:__spec.input,cx:__spec.complexity,
 th:__spec.theory,steps:T.events.length}));"""
        p = subprocess.run(['node', '-e', h], capture_output=True, text=True)
        if p.returncode: continue
        S = json.loads(p.stdout); th = S.get('th') or {}
        L = ['# %s. %s\n' % (S['num'], S['name']),
             '> **%s** &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; family: **%s**\n' % (S['difficulty'], md(S['pattern']), r['family']),
             '\n%s\n' % md(S.get('blurb','')),
             '\n**▶ [Step through this solution line by line](./visualization.html)** — %d steps, traced on `%s`.\n'
             % (S['steps'], md(S.get('input','')))]
        if S.get('cx'): L.append('\n| | |\n|---|---|\n| time | %s |\n| space | %s |\n' % (md(S['cx']['time']), md(S['cx']['space'])))
        if th.get('idea'): L.append('\n## The idea\n\n%s\n' % md(th['idea']))
        for key, title in (('recognize','How to recognise it'), ('pitfalls','Where people go wrong')):
            if th.get(key): L.append('\n## %s\n\n' % title + ''.join('- %s\n' % md(x) for x in th[key]))
        if th.get('template'): L.append('\n## The reusable template\n\n```python\n%s\n```\n' % th['template'].rstrip())
        if th.get('variants'):
            L.append('\n## If the interviewer twists it\n\n| Variant | What changes |\n|---|---|\n'
                     + ''.join('| %s | %s |\n' % (md(a), md(b)) for a, b in th['variants']))
        if th.get('thinking'): L.append('\n## How to think about it next time\n\n%s\n' % md(th['thinking']))
        L.append('\n---\n\n[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; '
                 '[pattern handbook](../PATTERNS.md)%s\n'
                 % ((' &nbsp;&middot;&nbsp; [on LeetCode](%s)' % S['url']) if S.get('url') else ''))
        io.open(note, 'w', encoding='utf-8').write(''.join(L))
        n += 1
    return n

def write_dojo(recs):
    import _check
    eng = io.open(os.path.join(ROOT, '_engine.js'), encoding='utf-8').read()
    TYPE_LABEL = {'push':'Make a choice / take a step deeper','pop':'Undo the last choice and back up',
      'found':'Record an answer or a new best','prune':'Abandon this branch — it cannot work',
      'skip':'Skip this option and try the alternative','dup':'Slide past a duplicate to avoid repeating work',
      'call':'Enter a new call / start the next iteration','bad':'Reject this candidate and move on',
      'ok':'Advance a pointer / commit the current state','info':'Just read the state — nothing changes yet',
      'done':'Finish and return the answer'}
    INTERESTING = ['push','pop','found','prune','skip','dup','bad']
    random.seed(7)
    problems = []
    for r in recs:
        if not r['page'] or not r['prompt']: continue
        body = '\n'.join(re.findall(r'<script>([\s\S]*?)</script>', io.open(r['page'], encoding='utf-8').read()))
        h = _check.STUB + eng + "\nvar __spec=null;LV.render=function(s){__spec=s;};\n" + body + """
var T=__spec.build();
console.log(JSON.stringify({num:__spec.num,name:__spec.name,slug:__spec.slug,pattern:__spec.pattern,
 input:__spec.input,src:__spec.src,tmpl:(__spec.theory&&__spec.theory.template)||'',
 ev:T.events.map(function(e){return {l:e.line,t:e.type,m:e.msg,v:e.vars};})}));"""
        p = subprocess.run(['node', '-e', h], capture_output=True, text=True)
        if p.returncode: continue
        S = json.loads(p.stdout); ev = S['ev']
        qs = []
        cand = [i for i in range(1, len(ev)-1) if ev[i+1]['t'] in INTERESTING]
        random.shuffle(cand); seen = set()
        for i in cand:
            nxt = ev[i+1]
            if nxt['t'] in seen and len(qs) >= 2: continue
            seen.add(nxt['t'])
            pool = [t for t in TYPE_LABEL if t != nxt['t'] and t != 'info']
            random.shuffle(pool)
            opts = [TYPE_LABEL[nxt['t']]] + [TYPE_LABEL[t] for t in pool[:3]]
            order = list(range(4)); random.shuffle(order)
            qs.append({'line': ev[i]['l'], 'vars': ev[i]['v'], 'story': [e['m'] for e in ev[max(0,i-2):i+1]],
                       'opts': [opts[k] for k in order], 'ans': order.index(0), 'why': nxt['m'], 'nline': nxt['l']})
            if len(qs) >= 3: break
        code = [(i, l) for i, l in enumerate(S['src'])
                if l.strip() and not l.strip().startswith(('#','//','/*','*','*/'))]
        parsons = ([{'i': i, 't': l.strip(), 'ind': (len(l)-len(l.lstrip()))//4} for i, l in code]
                   if 4 <= len(code) <= 20 else None)
        problems.append({'slug': r['slug'], 'num': r['num'], 'name': r['name'], 'pattern': S['pattern'],
                         'family': r['family'], 'difficulty': r['difficulty'], 'url': r['url'],
                         'prompt': r['prompt'], 'constraints': r['constraints'], 'example': r['example'],
                         'input': S['input'], 'src': S['src'], 'parsons': parsons,
                         'predict': qs, 'steps': len(ev), 'tmpl': S.get('tmpl','')})
    PREFERRED = {   # the problem whose template best represents each family
      'Backtracking':'0078-subsets','Two pointers & sliding window':'0003-longest-substring-without-repeating-characters',
      'Hashing':'0001-two-sum','Linked lists':'0206-reverse-linked-list',
      'Stacks & monotonic stacks':'0739-daily-temperatures','Binary search':'0704-binary-search',
      'Trees':'0124-binary-tree-maximum-path-sum','Graphs, BFS & DFS':'0773-sliding-puzzle',
      'Dynamic programming':'0070-climbing-stairs','Greedy':'0122-best-time-to-buy-and-sell-stock-ii',
      'Prefix sums & intervals':'0238-product-of-array-except-self','Bit manipulation':'0136-single-number',
      'Math & number theory':'1979-find-greatest-common-divisor-of-array','Design':'0146-lru-cache',
      'Sorting & divide and conquer':'0912-sort-an-array','Brute force done right':'3737-count-subarrays-with-majority-element-i'}
    templates = {}
    for p in problems:
        t = (p.get('tmpl') or '').strip()
        if not t: continue
        lines = [l for l in t.split('\n') if l.strip()]
        if not (5 <= len(lines) <= 22): continue
        cur = templates.get(p['family'])
        pref = PREFERRED.get(p['family'])
        better = (cur is None
                  or (pref and p['slug'] == pref)
                  or (not (pref and cur.get('slug') == pref) and len(t) > len(cur['tmpl'])))
        if better:
            templates[p['family']] = {'tmpl': t, 'from': '%d. %s' % (p['num'], p['name']), 'slug': p['slug']}
    data = {'families': FAM_NAMES, 'famdesc': FAM_DESC, 'problems': problems, 'templates': templates}
    io.open(os.path.join(ROOT, 'dojo-data.js'), 'w', encoding='utf-8').write(
        'window.DOJO = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')
    return len(problems)

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--new', action='store_true', help='only generate pages/notes that do not exist')
    ap.add_argument('--no-trace', action='store_true', help='skip auto-tracing new problems')
    a = ap.parse_args()

    print('scanning %s' % REPO)
    recs = scan()
    solved = [r for r in recs if r['solved']]
    missing = [r for r in solved if not r['page']]
    print('  %d problem folders, %d solved, %d already have a page, %d missing'
          % (len(recs), len(solved), len(solved)-len(missing), len(missing)))

    if missing and not a.no_trace:
        print('\nauto-tracing the new ones:')
        import trace as T
        for r in missing:
            out = T.trace_one(r['slug'], out=os.path.join(ROOT, r['slug'] + '.auto.html'))
            if out: r['page'] = out
        recs = scan()

    print('\nrebuilding:')
    print('  index.html            %d pages' % write_index(recs))
    print('  visualization.html    %d problem folders' % write_folder_pages(recs))
    print('  NOTES.md              %d written' % write_notes(recs, only_new=a.new))
    print('  dojo-data.js          %d problems in the trainer' % write_dojo(recs))
    print('\ndone.')

if __name__ == '__main__':
    main()
