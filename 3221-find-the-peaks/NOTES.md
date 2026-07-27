# 3221. Find the Peaks
> **Easy** &nbsp;·&nbsp; Array scan · local property &nbsp;·&nbsp; family: **Math & number theory**

A local-property scan. The interesting design choice is that the loop bounds encode the "endpoints cannot be peaks" rule, so no guard is needed inside the body.

**▶ [Step through this solution line by line](../visualizations/3221-find-the-peaks.html)** — 8 steps, traced on `mountain = [1,4,3,8,5]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) excluding the output |

## The idea

A **local property** is one you can verify by looking at a fixed-size neighbourhood. Peaks, valleys, plateau edges, "adjacent duplicates" — all decidable from a window of two or three, so a single scan suffices. Contrast with global properties (is this the maximum? is the array sorted?) which need the whole array before you can answer.

## How to recognise it

- The definition mentions only i−1, i, i+1 — that is the fingerprint.
- Boundary handling is the only real decision: either shrink the loop range (as here) or add guards inside.
- **But note:** if the question is "find ANY one peak" rather than all of them, binary search solves it in O(log n) — see LC 162. Same word, very different algorithm.

## Where people go wrong

- **Including index 0 and n−1.** They have one neighbour, so the comparison would index out of range or wrap negatively (Python’s `a[-1]` silently gives the last element — a wrong answer, not a crash).
- **Using `>=`.** A plateau [1,3,3,1] has no peak under a strict definition. Read the problem statement carefully.
- **The redundant `else: continue`.** Harmless, but it is noise — the loop continues anyway.
- **Confusing this with LC 162.** "Find a peak" in O(log n) is binary search on the slope; "find all peaks" cannot beat O(n).

## The reusable template

```python
# local property -> bounds encode the boundary rule, no guard needed
res = []
for i in range(1, len(a) - 1):        # endpoints excluded BY THE RANGE
    if a[i] > a[i-1] and a[i] > a[i+1]:
        res.append(i)
return res

# want ANY ONE peak instead of all? binary search on the slope, O(log n):
#   while lo < hi:
#       mid = (lo + hi) // 2
#       if a[mid] < a[mid+1]: lo = mid + 1     # rising -> a peak is right
#       else:                 hi = mid
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Find Peak Element** (LC 162) | Any one peak, O(log n) — binary search moving towards the rising side. |
| **Longest Mountain** (LC 845) | Expand outward from each peak. |
| **Valid Mountain Array** (LC 941) | Walk up, then walk down, and check you consumed everything. |
| **Total Waviness** (LC 3751 / 3753) | Peaks and valleys inside digit strings — digit DP. Also in your repo. |

## How to think about it next time

Two questions for any array-scan problem. **(1) How wide is the neighbourhood I need?** That determines the loop bounds and whether one pass is enough. **(2) Am I asked for ALL of them or just ONE?** "All" forces O(n); "any one" often opens the door to binary search on a local slope condition. Missing that second distinction is why people write O(n) for LC 162 and never notice.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/find-the-peaks)
