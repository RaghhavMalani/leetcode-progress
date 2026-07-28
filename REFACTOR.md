# Refactor queue

*Twelve solutions in this repo that are **accepted but worth rewriting**, ranked by how much the rewrite would
teach you. Every claim below was checked against the actual file — line numbers are real.*

Re-solving beats solving new problems more often than people expect: you already own the problem statement and the
debugging, so all of the effort goes into the idea you were missing.

---

## Tier 1 — rewrite these, they block transfer

### 1. `0046-permutations` — this is not backtracking

```python
perms = self.permute(nums[1:])      # line 6 — builds every sub-answer FIRST
```

You construct all permutations of the tail and then splice `nums[0]` into every gap. Correct, and it uses
O(n!·n) space instead of O(n).

**Why it matters more than the space:** bottom-up construction **cannot prune**. It builds every complete answer
and only then filters. The moment a problem adds a constraint — no two queens attacking, a sum target, a validity
rule — you need to abandon partial answers early, and that requires the shared-state-plus-undo shape.

**Do this:** rewrite it with `perm.append / dfs() / perm.pop()` and a `used[]` array, then diff it against your
[47](visualizations/0047-permutations-ii.html), which already uses the right skeleton. Ten minutes, and it unlocks
N-Queens, Sudoku Solver, and Word Search.

---

### 2. `0039-combination-sum` — the guard fires far too late

The file contains **no `sort()` and no `break`** (verified — zero matches). Every branch runs until the running
total overshoots.

**Open [the trace](visualizations/0039-combination-sum.html) and count the red nodes.** Most of that tree is
wasted work, and it is the direct contrast with [22](visualizations/0022-generate-parentheses.html), which has zero
dead ends.

**Do this:**

```python
nums.sort()                                    # add this
...
    for i in range(start, len(nums)):
        if total + nums[i] > target:
            break                              # and this — every later one is bigger too
```

The tree collapses. This is the single most transferable idea in backtracking: *sorting is what makes an early
impossibility test possible*.

---

### 3. `0705-design-hashset` — `remove` never removes

```python
def remove(self, key): self.hashset[key] = 0    # line 10 — a tombstone, not a deletion
```

Under an add/remove-heavy workload the dictionary grows without bound. `del self.hashset[key]` is the fix.

**But the real point:** the problem asks you to *implement* a hash set, and this wraps Python's. You get no practice
with buckets, collisions, chaining, or load factor — which is what the interview follow-ups are about.

**Do this:** `buckets = [[] for _ in range(1000)]`, `idx = hash(key) % 1000`, scan the chain. Then answer aloud:
what is the average cost, the worst case, what triggers the worst case, and when do you resize?

---

### 4. `0706-design-hashmap` — same story

```python
def __init__(self): self.hashmap = {}           # line 4
```

Same rewrite as 705, with `(key, value)` pairs in the buckets and **overwrite-or-append** on `put`. Do the two
together; the second takes five minutes once the first is done.

Also worth saying out loud: the `-1` sentinel for a missing key means you can never store `-1`. Real APIs return
`None`, raise, or take a default.

---

## Tier 2 — real defects, small fixes

### 5. `0703-kth-largest-element-in-a-stream` — mutates the caller's list

```python
self.minHeap = nums                             # line 4 — an alias, not a copy
heapq.heapify(self.minHeap)                     # reorders the caller's list in place
```

The constructor silently rearranges (and then pops from) the list the caller handed you. On LeetCode nobody
notices; in real code it is a nasty bug and in an interview it is a free point for whoever spots it.

**Fix:** `self.minHeap = list(nums)`.

---

### 6. `0463-island-perimeter` — recursion depth, and a simpler answer exists

```python
perim = dfs(i+1,j)                              # lines 14–17, four-way recursion
```

A 100×100 all-land grid is 10,000 frames deep; Python's default limit is 1,000. Convert to an explicit stack, or —
better — notice that no search is needed at all:

```python
# perimeter = 4 * (land cells) - 2 * (adjacent land pairs)
```

One pass, O(cells), no recursion, no visited set. **Give the O(1)-space counting answer first**, then mention DFS
as the general tool when the problem stops being about a single island.

---

### 7. `0912-sort-an-array` — allocates on every level

```python
left_half  = mergesort(arr[:mid])               # lines 32–33
right_half = mergesort(arr[mid:])
```

Each slice copies. Across log n levels that is O(n log n) *allocation* on top of the comparisons — the constant
factor is much worse than it looks.

**Fix:** pass `(lo, hi)` indices into a shared buffer, and merge into a scratch array reused across calls. Worth
doing once so you know what "in place" actually costs.

---

### 8. `0036-valid-sudoku` — a `defaultdict` side effect

```python
if (board[row][col] in rows[row] or ...)        # line 16
```

`rows[row]` on a `defaultdict(set)` **creates an empty set as a side effect of the membership test**. Harmless on a
9×9 board, a genuine leak in long-running code. Use a plain `dict` with `.get(row, EMPTY)`, or pre-size the arrays.

**Then upgrade it:** nine bits per row / column / box in three integer arrays. O(1) space, faster, and it is the
answer the interviewer is hoping for.

---

### 9. `1071-greatest-common-divisor-of-strings` — O(n·m) where O(n) exists

```python
for l in range(min(l1,l2),0,-1):                # line 13 — tries every candidate length
```

There is a two-line version:

```python
if s1 + s2 != s2 + s1: return ""                # they must commute, or no divisor exists
return s1[:gcd(len(s1), len(s2))]
```

Your version is fine for the constraints, but the commuting argument is a lovely piece of reasoning and worth
owning. See [the notes](1071-greatest-common-divisor-of-strings/NOTES.md).

---

## Tier 3 — style and follow-ups, not bugs

### 10. `0124-binary-tree-maximum-path-sum` — the list hack

```python
res = [root.val]                                # line 14
```

A one-element list so the nested function can mutate it. This works everywhere, but in Python 3 `nonlocal res` says
what you mean. Know both — the list trick is what you fall back on in Python 2 or in a lambda.

---

### 11. `2133-number-of-pairs-...` — say the linear version out loud

Two nested loops (verified). That is the **intended** answer at n ≤ 100, so do not change it — but be able to state
the alternative: split `target` at every position and multiply `count[prefix] × count[suffix]`, subtracting the
self-pairs when prefix == suffix. O(n·L).

---

### 12. `1291-sequential-digits` — an unnecessary sort

```cpp
sort(ans.begin(), ans.end());                   // line 17
```

The generation loop runs length-outermost, and a longer sequential number is always larger, so the results come out
sorted already. The sort is harmless (36 elements) but it signals you did not notice. Either delete it, or keep it
and say *"belt and braces — the generation order happens to be sorted, but I would rather not rely on it."* Both
are good answers; saying nothing is not.

---

## How to work this list

Do **Tier 1 in order** — those four are about ideas that transfer, not about tidiness. Tier 2 in one sitting; they
are ten minutes each. Tier 3 only needs reading.

After each rewrite, regenerate the trace so the visualization matches the new code:

```bash
cd visualizations
python3 _check.py          # confirms every page still builds and its source matches the repo
```

If a page's embedded source no longer matches its `.py`, `_check.py` is not the thing that will tell you — the
source is baked in at build time. Re-run the generator for that problem, or ping me to rebuild it.

---

[← traced solutions](visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](PATTERNS.md) &nbsp;·&nbsp;
[study plan](STUDY-PLAN.md) &nbsp;·&nbsp; [the Dojo](visualizations/dojo.html)
