# 867. New 21 Game
> **Medium** &nbsp;&middot;&nbsp; Probability DP · sliding window sum &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

A DP whose recurrence sums a fixed-width window of earlier states. Recomputing that sum is O(n·maxPts); maintaining it incrementally is O(n) — and that pattern generalises far beyond this problem.

**▶ [Step through this solution line by line](./visualization.html)** — 20 steps, traced on `n = 6, k = 4, maxPts = 3`.

| | |
|---|---|
| time | O(n) — the window sum makes it linear |
| space | O(n), reducible to O(maxPts) |

## The idea

Two ideas. **Probability DP:** dp[i] is the probability of ever reaching exactly i, and it is the average of the previous maxPts states because each draw is uniform. **Rolling window sum:** when a recurrence sums a contiguous window of previous states, maintain the sum with one add and one subtract per step instead of re-summing.

## How to recognise it

- A recurrence of the form `dp[i] = f(dp[i-1] … dp[i-w])` where w is fixed. Sum → rolling sum. Max → monotonic deque. Min → the same deque, flipped.
- Probability questions where each step has uniformly random outcomes.
- The two-region structure — states you continue from, states you stop at — is common in absorbing-state problems.

## Where people go wrong

- **Adding terminal states to the window.** Once i ≥ k the game stops, so dp[i] must never feed a later dp. Getting this wrong is the conceptual error that makes the answer exceed 1.
- **Forgetting to subtract the element that leaves the window.** Line 19–20. Without it the window keeps growing and every probability is wrong.
- **Missing the early return.** When `n >= k + maxPts` you cannot bust, so the answer is exactly 1.0 — and without that guard the loop may not even be well defined.
- **Float accumulation.** Fine at these sizes, but be aware you are summing thousands of small floats.

## The reusable template

```python
# DP whose transition sums a fixed window -> keep the sum rolling
dp = [0.0] * (n + 1); dp[0] = 1.0
window = 1.0          # sum of dp[i-maxPts .. i-1], but only over DRAWING states
res = 0.0

for i in range(1, n + 1):
    dp[i] = window / maxPts
    if i < k:  window += dp[i]     # still drawing -> it can feed later states
    else:      res    += dp[i]     # terminal -> counts as an answer, NOT in window
    if i >= maxPts:
        window -= dp[i - maxPts]   # slid out of range
return res

# window is a MAX instead of a sum? use a monotonic deque.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Climbing Stairs** (LC 70) | The same fixed-window recurrence with w = 2 and no division. Also in your repo. |
| Sliding window MAX in a DP | Monotonic deque instead of a running sum — e.g. LC 1696 Jump Game VI. |
| **Knight Probability in Chessboard** (LC 688) | Probability DP over a grid, no window trick needed. |
| **Number of Zigzag Arrays** (LC 3699) | Prefix sums inside a DP transition. Also in your repo. |

## How to think about it next time

Whenever you write a DP, look at the transition and ask **"is this a sum or an extremum over a contiguous window of previous states?"** If yes, you can almost always drop a factor of w: running sum for sums, monotonic deque for max/min, prefix sums when the window varies. That single observation is the difference between an accepted solution and a TLE in a large fraction of medium DP problems.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/new-21-game)
