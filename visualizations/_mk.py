# -*- coding: utf-8 -*-
"""Wraps a per-problem JS spec into a standalone HTML page and injects the
   real solution source (read straight from the repo) as the src array."""
import io, os, json, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)

HEAD = u'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="stylesheet" href="_engine.css">
</head>
<body>
<script src="_engine.js"></script>
<script>
'''
TAIL = u'''
</script>
</body>
</html>
'''

def srclines(slug, ext=None):
    d = os.path.join(REPO, slug)
    cands = []
    for e in ([ext] if ext else ['py','cpp','java','c']):
        cands += sorted(glob.glob(os.path.join(d, '*.'+e)))
        if cands: break
    if not cands:
        raise IOError('no solution file for '+slug)
    txt = io.open(cands[0], encoding='utf-8').read().replace('\t','    ').rstrip()
    return txt.split('\n')

def src_js(slug, ext=None):
    return json.dumps(srclines(slug, ext), ensure_ascii=False)

def page(slug, title, js):
    js = js.replace('__SRC__', src_js(slug))
    out = os.path.join(ROOT, slug + '.html')
    io.open(out, 'w', encoding='utf-8').write(HEAD % title + js + TAIL)
    return out
