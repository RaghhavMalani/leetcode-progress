# 2133. Number of Pairs of Strings With Concatenation Equal to Target
> **Medium** &nbsp;&middot;&nbsp; Brute force · index vs value identity &nbsp;&middot;&nbsp; family: **Brute force done right**

A double loop, deliberately. The subtlety is the `i == j` guard: two *equal strings at different indices* are a legal pair, but an element may not pair with itself.

**▶ [Step through this solution line by line](./visualization.html)** — 18 steps, traced on `nums = ["777","7","77","77"], target = "7777"`.

| | |
|---|---|
| time | O(n² · L) |
| space | O(1) |

## The idea

The lesson here is about **identity**. "Distinct elements" almost always means distinct *indices*, not distinct *values*. Skipping on `nums[i] == nums[j]` instead of `i == j` silently drops the duplicate pairs this problem is built around.

## How to recognise it

- Small n (≤ 100) with a pairwise condition — the constraints are telling you O(n²) is intended.
- "Pairs (i, j) where i ≠ j" and the pair is ORDERED, so (a,b) and (b,a) both count.
- The O(n) version exists: for each valid split of target into prefix + suffix, multiply the counts. Worth mentioning even when not required.

## Where people go wrong

- **Skipping when the values are equal.** ["77","77"] with target "7777" has TWO valid pairs, and this bug reports zero.
- **Counting unordered pairs.** The problem asks for ordered (i, j), so do not halve.
- **Length pre-check as an optimisation.** `len(a) + len(b) != len(target)` rejects most pairs in O(1) — a free speedup worth adding.
- **Believing O(n²) is a weakness.** Here it is the intended answer; say the O(n·L) alternative exists and move on.

## The reusable template

```python
# ORDERED pairs of distinct INDICES (not distinct values)
count = 0
for i in range(n):
    for j in range(n):
        if i == j:                      # index identity, NOT nums[i] == nums[j]
            continue
        if len(nums[i]) + len(nums[j]) != len(target):   # free O(1) reject
            continue
        if nums[i] + nums[j] == target:
            count += 1

# O(n*L) version: for each split of target, multiply the two counts
#   (subtract the self-pair when prefix == suffix)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| O(n·L) counting version | Split target at every position; multiply `count[prefix] × count[suffix]`, subtracting the self-pairs when prefix == suffix. |
| **Two Sum** (LC 1) | The same index-vs-value distinction, solved with a hash map. Also in your repo. |
| Count pairs with a given sum | `ans += seen[target - x]` before inserting x — order matters, exactly as in Two Sum. |
| Unordered pairs | Loop `j` from `i+1`, and the count halves. |

## How to think about it next time

Whenever a problem says "two elements", stop and decide whether it means **two positions** or **two values**. That single distinction is behind a large share of wrong answers on pair-counting problems — including the classic Two Sum edge case with `[3,3]`. Write the guard as `i != j` by default, and only switch to a value comparison if the statement explicitly asks for distinct values.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target)
