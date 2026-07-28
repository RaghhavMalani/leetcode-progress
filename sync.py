#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync.py — pull your new solves from GitHub and regenerate everything.

    python sync.py              # the normal run
    python sync.py --no-pull    # just rebuild from what is already on disk
    python sync.py --dry        # say what would happen, change nothing

What it does, in order:
  1. clears a stale .git/index.lock (the thing that silently blocks every git command)
  2. commits whatever you have locally, so nothing is ever lost to a rebase
  3. git pull --rebase origin <branch>
  4. finds problem folders that have a solution but no visualization
  5. traces each one by actually running it, and writes its NOTES.md
  6. rebuilds the index, the per-folder pages and the Dojo dataset

Line endings: this repo carries a .gitattributes with `* text=auto`. Without it a
Windows checkout makes every file look modified and git refuses to pull at all.
Do not delete it.
"""
import io, os, re, sys, time, argparse, subprocess

REPO = os.path.dirname(os.path.abspath(__file__))
VIS  = os.path.join(REPO, 'visualizations')

C = {'r':'\033[31m','g':'\033[32m','y':'\033[33m','c':'\033[36m','d':'\033[2m','x':'\033[0m'}
if os.name == 'nt' and not os.environ.get('WT_SESSION'):
    try:                                   # enable ANSI on older Windows terminals
        import ctypes; ctypes.windll.kernel32.SetConsoleMode(
            ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        C = {k: '' for k in C}

def say(msg, col='x'): print('%s%s%s' % (C[col], msg, C['x']))
def step(n, msg):      say('\n[%s] %s' % (n, msg), 'c')

def git(*args, check=False, quiet=True):
    p = subprocess.run(['git'] + list(args), cwd=REPO, capture_output=True, text=True)
    out = (p.stdout + p.stderr)
    if not quiet and out.strip():
        for line in out.strip().split('\n'):
            if line.startswith('warning: LF') or line.startswith('The file will have'): continue
            print('    ' + line)
    if check and p.returncode:
        raise RuntimeError('git %s failed:\n%s' % (' '.join(args), out))
    return p.returncode, out

# ------------------------------------------------------------------ 1. lock
def clear_stale_lock(dry=False):
    lock = os.path.join(REPO, '.git', 'index.lock')
    if not os.path.exists(lock): return False
    age = time.time() - os.path.getmtime(lock)
    say('    found .git/index.lock (%.0f s old)' % age, 'y')
    if dry: return True
    try:
        os.remove(lock)
        say('    removed it — this is what was blocking git', 'g')
        return True
    except Exception as e:
        say('    could NOT remove it: %s' % e, 'r')
        say('    delete it by hand, then run this again:', 'r')
        say('      del "%s"' % lock.replace('/', '\\'), 'r')
        sys.exit(1)

# ------------------------------------------------------------------ helpers
def current_branch():
    _, out = git('rev-parse', '--abbrev-ref', 'HEAD')
    return out.strip() or 'main'

def solved_folders():
    out = []
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d)
        if not (re.match(r'^\d{4}-', d) and os.path.isdir(p)): continue
        if any(f.endswith(('.py', '.cpp', '.java', '.c')) for f in os.listdir(p)):
            out.append(d)
    return out

def without_pages(folders):
    return [d for d in folders
            if not os.path.exists(os.path.join(VIS, d + '.html'))
            and not os.path.exists(os.path.join(VIS, d + '.auto.html'))]

# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-pull', action='store_true', help='skip git entirely, just rebuild')
    ap.add_argument('--dry', action='store_true', help='report only, change nothing')
    ap.add_argument('--push', action='store_true', help='push at the end (needs your credentials)')
    a = ap.parse_args()

    say('\n  leetcode-progress · sync', 'c')
    say('  ' + REPO, 'd')

    before = set(solved_folders())
    say('\n  %d solved problems on disk, %d with a visualization'
        % (len(before), len(before) - len(without_pages(before))))

    if not a.no_pull:
        step(1, 'checking for a stale git lock')
        if not clear_stale_lock(a.dry): say('    none — good', 'd')

        step(2, 'saving your local work')
        _, st = git('status', '--porcelain')
        dirty = [l for l in st.strip().split('\n') if l.strip()]
        if dirty:
            say('    %d files to commit' % len(dirty))
            if not a.dry:
                git('add', '-A')
                rc, _ = git('commit', '-m', 'Local work before sync')
                say('    committed' if rc == 0 else '    nothing needed committing', 'd')
        else:
            say('    working tree already clean', 'd')

        step(3, 'pulling from origin')
        br = current_branch()
        git('fetch', 'origin', quiet=True)
        rc, out = git('rev-list', '--count', 'HEAD..origin/%s' % br)
        n = out.strip() if out.strip().isdigit() else '?'
        say('    %s commits waiting on origin/%s' % (n, br))
        if a.dry:
            say('    (dry run — not pulling)', 'd')
        elif n not in ('0', '?'):
            rc, out = git('-c', 'core.autocrlf=true', 'pull', '--rebase', 'origin', br, quiet=False)
            if rc:
                say('\n    the pull did not complete. Most likely a conflict in README.md,', 'r')
                say('    which LeetHub rewrites on every solve. To take their version:', 'r')
                say('      git checkout --theirs README.md && git add README.md && git rebase --continue', 'r')
                sys.exit(1)
            say('    up to date', 'g')
        else:
            say('    already up to date', 'd')

    after = set(solved_folders())
    fresh = sorted(after - before)
    if fresh:
        step(4, 'new problems arrived')
        for d in fresh: say('    + ' + d, 'g')
    else:
        step(4, 'no new problem folders')

    todo = without_pages(after)
    if todo:
        say('    %d solved problem%s without a visualization:' % (len(todo), '' if len(todo) == 1 else 's'))
        for d in todo[:12]: say('      ' + d, 'd')
        if len(todo) > 12: say('      … and %d more' % (len(todo) - 12), 'd')
    else:
        say('    every solved problem already has one', 'd')

    if a.dry:
        say('\n  dry run — nothing was changed.', 'y'); return

    step(5, 'tracing and rebuilding')
    rc = subprocess.call([sys.executable, os.path.join(VIS, 'build.py')], cwd=VIS)
    if rc:
        say('    build.py failed', 'r'); sys.exit(1)

    step(6, 'verifying')
    subprocess.call([sys.executable, os.path.join(VIS, '_check.py')], cwd=VIS)

    if a.push and not a.dry:
        step(7, 'committing and pushing')
        git('add', '-A')
        git('commit', '-m', 'Regenerate visualizations after sync')
        rc, out = git('push', 'origin', current_branch(), quiet=False)
        say('    pushed' if rc == 0 else '    push failed — check your credentials', 'g' if rc == 0 else 'r')

    say('\n  done. Open visualizations/index.html or visualizations/dojo.html\n', 'g')

if __name__ == '__main__':
    main()
