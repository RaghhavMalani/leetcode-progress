# 304. Range Sum Query 2D — Immutable
> **Medium** &nbsp;·&nbsp; 2D prefix sum · inclusion–exclusion &nbsp;·&nbsp; family: **Prefix sums & intervals**

Prefix sums in two dimensions. Both the build and the query are inclusion–exclusion — add two overlapping regions, subtract the double-counted overlap — and the padded border makes every index safe.

**▶ [Step through this solution line by line](../visualizations/0304-range-sum-query-2d-immutable.html)** — 25 steps, traced on `a 4×4 matrix, then three sumRegion queries`.

| | |
|---|---|
| time | O(m·n) to build, **O(1) per query** |
| space | O(m·n) |

## The idea

A prefix table stores, at every cell, the sum of everything above and to the left of it. Any rectangle is then four reads: the big corner, minus the strip above, minus the strip to the left, plus the corner region you just subtracted twice. That last `+` is **inclusion–exclusion**, and it is the only part people get wrong.

## How to recognise it

- **Many queries, immutable data.** That combination always means "precompute". The word "Immutable" in the title is a direct hint.
- "Sum / count over a range" repeated many times.
- If the data *changes*, prefix sums die and you need a Fenwick tree or segment tree — that is LC 308.

## Where people go wrong

- **Not padding the table.** Without the extra row and column you need `if r > 0` guards in four places. The +1 border costs one row of memory and removes them all.
- **Sign errors.** Build is `+cell +above +left −diag`; query is `+big −above −left +corner`. Draw the four rectangles once and you will never mix them up.
- **Off-by-one between matrix and prefix coordinates.** `prefix[r+1][c+1]` corresponds to `matrix[r][c]`. Keeping that one line of translation explicit in your head is most of the battle.
- **Recomputing the table on each query.** Defeats the entire purpose.

## The reusable template

```python
# 2D prefix sum - pad by one so there are no boundary branches
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for r in range(m):
    for c in range(n):
        prefix[r+1][c+1] = (matrix[r][c]
                            + prefix[r][c+1]     # everything above
                            + prefix[r+1][c]     # everything left
                            - prefix[r][c])      # counted twice -> remove once

def sumRegion(r1, c1, r2, c2):
    return (prefix[r2+1][c2+1]
            - prefix[r1][c2+1]                   # strip above
            - prefix[r2+1][c1]                   # strip left
            + prefix[r1][c1])                    # subtracted twice -> add back

# 1D version, learn this first:  prefix[j+1] - prefix[i]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| 1D range sum | LC 303 — `prefix[j+1] - prefix[i]`. Learn this one first. |
| **Mutable** 2D range sum | LC 308 — 2D Fenwick tree, O(log m · log n) per update and query. |
| **Subarray Sum Equals K** (LC 560) | Prefix sums plus a hash map of counts — the same complement trick as Two Sum. |
| **Max Sum Rectangle ≤ K** (LC 363) | Fix a pair of columns, collapse to 1D, then a sorted-prefix search. |
| Count of range sums | LC 327 — prefix sums plus merge sort or a BIT. |

## How to think about it next time

Prefix sums are the answer to "**many range queries over static data**", and the pattern generalises far beyond sums: prefix XOR, prefix max (via sparse tables), prefix counts of a character, prefix products (LC 238 in your repo). The general question to ask is: *can I precompute a value at every position such that any range answer is a cheap combination of two or four of them?* If the operation has an inverse — sum, XOR, product with no zeros — the answer is yes.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable)
