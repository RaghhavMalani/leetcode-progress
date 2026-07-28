# 3739. Count Subarrays With Majority Element II
> **Hard** &nbsp;&middot;&nbsp; +1/−1 transform · prefix sums · Fenwick tree &nbsp;&middot;&nbsp; family: **Prefix sums & intervals**

Three techniques composed. Map target to +1 and everything else to −1; "majority" becomes "positive sum"; counting those becomes an inversion count, which a Fenwick tree does in O(n log n).

**▶ [Step through this solution line by line](./visualization.html)** — 16 steps, traced on `nums = [1,2,1,1], target = 1`.

| | |
|---|---|
| time | O(n log n) |
| space | O(n) |

## The idea

Three moves, each standard on its own. **(1) The ±1 transform** converts a counting condition ("more than half") into an arithmetic one ("sum > 0"). **(2) Prefix sums** convert a subarray condition into a condition on two endpoints. **(3) A Fenwick tree** counts, for each j, how many earlier prefixes are smaller — the inversion-count primitive.

## How to recognise it

- "More X than Y in a range" → ±1 transform, every time. It also solves LC 525 (equal 0s and 1s) and LC 1524.
- "Count pairs i < j with p[i] < p[j]" → Fenwick tree, merge sort, or an order-statistics tree.
- Part I with n ≤ 1000 permits O(n²); this version with n ≤ 10⁵ does not. The escalation is the point.

## Where people go wrong

- **Forgetting to seed prefix 0.** Every subarray beginning at index 0 is lost. Line 30.
- **Negative or zero Fenwick indices.** A BIT is 1-indexed; the `offset` shift is mandatory, and it must be big enough for the most negative prefix (−n).
- **Querying `idx` instead of `idx - 1`.** You need STRICTLY less, so exclude equal prefixes — equal would mean a sum of exactly 0, which is a tie, not a majority.
- **Inserting before querying.** A prefix would be counted against itself.
- **Getting `idx & -idx` backwards.** Update walks upward with `+=`, query walks downward with `-=`. Mixing them silently corrupts everything.

## The reusable template

```python
# 1. +/-1 transform:  "majority" -> "sum > 0" -> "prefix[j] > prefix[i]"
# 2. Fenwick tree counts, for each j, how many earlier prefixes are smaller.

class Fenwick:
    def __init__(self, n): self.b = [0] * (n + 1)
    def add(self, i, v):
        while i < len(self.b): self.b[i] += v; i += i & -i     # UP
    def query(self, i):
        t = 0
        while i > 0: t += self.b[i]; i -= i & -i               # DOWN
        return t

offset = n + 2                       # prefix ranges over [-n, n]; BIT is 1-indexed
bit, prefix, ans = Fenwick(2*n + 5), 0, 0
bit.add(prefix + offset, 1)          # SEED the empty prefix. do not skip.

for x in nums:
    prefix += 1 if x == target else -1
    ans += bit.query(prefix + offset - 1)   # STRICTLY smaller -> the -1
    bit.add(prefix + offset, 1)             # insert AFTER querying
return ans
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part I** (LC 3737) | n ≤ 1000, so the O(n²) double loop is intended. Also in your repo. |
| **Contiguous Array** (LC 525) | Equal 0s and 1s → same ±1 transform, then a hash map of first-seen prefix. |
| **Count of Smaller Numbers After Self** (LC 315) | The same inversion count, usually via merge sort. |
| Count subarrays with sum ≥ k | Prefix sums plus a BIT, or a sliding window when all values are positive. |
| Merge sort instead of a BIT | Same O(n log n), no index shifting to get wrong. |

## How to think about it next time

This problem is a good model of how Hard problems are built: **a chain of three standard reductions**, none hard alone. Practise naming the chain out loud — "majority becomes positive sum, positive sum becomes a prefix comparison, prefix comparison becomes inversion counting" — because that is exactly what you would say in an interview before writing anything. When a Hard problem looks impossible, look for the first reduction rather than the whole solution; the second and third usually become obvious once the first lands.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii)
