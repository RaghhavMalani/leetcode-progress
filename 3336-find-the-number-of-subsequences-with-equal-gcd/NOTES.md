# 3336. Find the Number of Subsequences With Equal GCD
> **Hard** &nbsp;·&nbsp; DP over a bounded state (gcd × gcd) &nbsp;·&nbsp; family: **Dynamic programming**

The state is a *pair of gcds*, not a pair of subsets. Because every gcd of the input divides some value ≤ 200, the state space is only 201×201 — that bound is what makes an exponential problem polynomial.

**▶ [Step through this solution line by line](../visualizations/3336-find-the-number-of-subsequences-with-equal-gcd.html)** — 51 steps, traced on `nums = [1,2,3]`.

| | |
|---|---|
| time | O(n · V²) with V = 200 |
| space | O(V²) |

## The idea

The trick is **choosing a state that is small enough to enumerate**. You cannot track which elements went into each group — that is 3ⁿ. But you only ever *need* the two gcds, and gcds of values ≤ 200 are themselves ≤ 200. So the state collapses from exponential to 201² and a DP becomes possible.

## How to recognise it

- Counting subsets or partitions where the condition depends on an **aggregate** (gcd, sum, xor, max) rather than on the identity of the elements.
- Small value bounds in the constraints (here 200) — that number is the size of your state dimension, and it is always deliberate.
- The three-way "skip / group A / group B" branch is the standard shape for partitioning into two labelled groups.

## Where people go wrong

- **Updating `dp` in place.** An element could then be added to a state that already includes it. The fresh `next` table is mandatory — this is the same discipline as 0/1 knapsack iterating backwards.
- **Including gcd 0 in the final sum.** gcd 0 means the group is empty, and both groups must be non-empty. Line 46 starts at 1.
- **Forgetting the modulus** on every addition, not just at the end.
- **Allocating a fresh 201×201 table per element without the `if dp == 0: continue` skip.** Most states are unreachable; skipping them is what keeps it fast in practice.
- **Double counting.** The groups here are labelled (group 1 vs group 2), so (A, B) and (B, A) are distinct — check whether the problem wants that.

## The reusable template

```python
# state = (gcd of group 1, gcd of group 2). bounded by max value, so 201x201.
dp = [[0] * (V + 1) for _ in range(V + 1)]
dp[0][0] = 1                       # gcd of an EMPTY group is 0 (the identity)

for x in nums:
    nxt = [[0] * (V + 1) for _ in range(V + 1)]     # FRESH table, never in place
    for g1 in range(V + 1):
        for g2 in range(V + 1):
            w = dp[g1][g2]
            if not w: continue                       # most states are unreachable
            nxt[g1][g2]        = (nxt[g1][g2] + w) % MOD          # skip x
            nxt[gcd(g1,x)][g2] = (nxt[gcd(g1,x)][g2] + w) % MOD   # x -> group 1
            nxt[g1][gcd(g2,x)] = (nxt[g1][gcd(g2,x)] + w) % MOD   # x -> group 2
    dp = nxt

return sum(dp[g][g] for g in range(1, V + 1)) % MOD   # from 1: skip empty groups
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Sum instead of gcd | Subset-sum DP — the state is the sum, bounded by n × maxValue. |
| XOR instead of gcd | State is the xor value, bounded by the next power of two. |
| Three groups | A three-dimensional state, V³ — check the bound before committing. |
| **Subsequences with equal sum** | Classic partition DP; same skip/A/B branch. |

## How to think about it next time

The single most useful question in DP design is **"what is the smallest piece of information about the past that determines the future?"** Here it is not the subsets but their two gcds. Then check the second question: **is that state space small enough to enumerate?** The constraint "values ≤ 200" is the problem telling you the answer is yes. When you see a suspiciously small value bound in a counting problem, it is almost always the dimension of the intended DP state.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd)
