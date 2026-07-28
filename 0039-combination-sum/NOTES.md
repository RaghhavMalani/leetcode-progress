# 39. Combination Sum
> **Medium** &nbsp;&middot;&nbsp; Backtracking · take / skip &nbsp;&middot;&nbsp; family: **Backtracking**

The mirror image of problem 22. Here the guard fires only *after* the total has already overshot, so the algorithm discovers its mistakes instead of preventing them. Look at how much red is in that tree.

**▶ [Step through this solution line by line](./visualization.html)** — 168 steps, traced on `nums = [2,3,6,7], target = 7`.

| | |
|---|---|
| time | O(2^(target/min(nums))) in the worst case — every node branches take/skip |
| space | O(target/min(nums)) recursion depth |

## The idea

This is the **take / skip** shape of backtracking: at every index you make one binary decision — use this number, or move past it forever. The one character that makes this problem special is `dfs(i, …)` instead of `dfs(i+1, …)` on the take branch: staying on the same index is what allows a number to be reused unlimited times.

## How to recognise it

- "Find all combinations that sum to X" and **order does not matter** — [2,2,3] and [3,2,2] are the same answer.
- Elements may be **reused**. That is the tell for recursing on `i`; if each element were single-use you would recurse on `i+1` (that is LC 40).
- Small constraints (`len(nums) ≤ 30`, target ≤ 40) — the interviewer is licensing exponential search.
- You are asked for the **combinations themselves**. If asked only *how many ways*, this becomes unbounded-knapsack DP in O(n · target).

## Where people go wrong

- **Recursing on `i+1` on the take branch.** Silently turns this into LC 40 and you lose every answer that reuses a value.
- **Forgetting `.copy()`.** `res.append(curr)` stores a live reference; by the end every entry in res is the same empty list.
- **Checking `total == target` after the overshoot check.** Order matters — if you test `total > target` first and your target is hit exactly, you are fine, but flipping to `total ≥ target` loses the exact hits.
- **Not sorting + not breaking early.** With `nums.sort()` you can `break` the moment `total + nums[i] > target`, which prunes most of the red in that tree. Your version is correct but does strictly more work.

## The reusable template

```python
# Backtracking skeleton. Every problem in this family is this shape.
def backtrack(state):
    if is_complete(state):
        res.append(path.copy())      # COPY - path keeps mutating
        return
    if is_impossible(state):         # prune BEFORE you descend
        return
    for choice in choices(state):
        path.append(choice)          # 1. choose
        backtrack(advance(state))    # 2. explore
        path.pop()                   # 3. un-choose
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Each number usable **once**, input has duplicates | LC 40 — recurse on `i+1` and sort so you can skip equal neighbours on the skip branch. |
| Only **count** the combinations | Unbounded knapsack DP: `dp[t] += dp[t - num]`, O(n·target). No recursion at all. |
| Order **does** matter ([2,3] ≠ [3,2]) | LC 377 Combination Sum IV — the loop moves inside: `dp[t] = Σ dp[t-num]`. This is a genuinely different count. |
| Fixed length k, digits 1..9 only | LC 216 — same skeleton, extra guard `len(curr) == k`. |

## How to think about it next time

Put 22 and 39 side by side. Both are the same skeleton; the only difference is **when you can tell a branch is doomed**. In 22 the counters tell you before you descend, so nothing is wasted. In 39 you only learn after the total overshoots. Whenever you write a backtracking solution, ask: *what is the cheapest test that proves this branch cannot possibly work?* Then move it as early as you can. Sorting the input is very often what makes such a test possible, because it lets you conclude "if this one is too big, all the rest are too".

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/combination-sum)
