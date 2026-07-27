# 2503. Longest Subarray With Maximum Bitwise AND
> **Medium** &nbsp;·&nbsp; Observation-driven · monotone operation &nbsp;·&nbsp; family: **Greedy**

A problem where the code is trivial once you notice one fact: AND never increases. That reduces the whole thing to "find the longest run of the maximum value".

**▶ [Step through this solution line by line](../visualizations/2503-longest-subarray-with-maximum-bitwise-and.html)** — 21 steps, traced on `nums = [1,2,3,3,2,2]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

**AND is monotone decreasing**: adding an element to a subarray can only clear bits, never set them. So the largest achievable AND equals `max(nums)`, and it is achieved only by subarrays consisting entirely of that maximum. Everything else in the problem statement is scenery.

## How to recognise it

- Bitwise AND/OR over subarrays. AND only shrinks; OR only grows. That monotonicity is almost always the intended insight.
- When a problem asks for "the maximum of some aggregate", ask first **what the maximum possible value even is** — often the answer bounds the search dramatically.
- Contrast: OR over subarrays (LC 898, in your repo) grows, so runs do not help and you need the set-of-distinct-ORs trick.

## Where people go wrong

- **Actually computing ANDs over all subarrays.** O(n²) and completely unnecessary.
- **Forgetting `res = 0` when a new maximum appears.** The subtlest line here. A long run of 2s must be discarded the moment a 3 shows up.
- **Handling the run-break as `size = 1`.** It is 0 — the current element is not part of any max run.
- **Two passes (find max, then find the longest run) is also fine** and arguably clearer. Say so; the single pass is a small optimisation, not a requirement.

## The reusable template

```python
# AND never increases -> the best possible AND is max(nums),
# achieved only by a run of copies of that maximum.
size = res = curmax = 0
for n in nums:
    if n > curmax:
        curmax, size, res = n, 1, 0    # NEW max invalidates old runs: res = 0
    elif n == curmax:
        size += 1
    else:
        size = 0                        # run broken
    res = max(res, size)
return res

# two-pass version is just as good:  m = max(nums), then longest run of m
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Bitwise ORs of Subarrays** (LC 898) | OR grows, so you keep the set of distinct ORs ending at each index — at most 32 of them. Also in your repo. |
| Longest subarray with AND ≥ k | Now you do need a sliding window or a bit-count trick — monotonicity helps but does not collapse it. |
| **Longest Subarray with Maximum GCD** | Same shape: GCD is also non-increasing under extension. |
| Maximum AND of any two elements | LC 2429-style — build the answer bit by bit from the top. |

## How to think about it next time

Before writing any loop, ask **"what is the best value that is even possible, and what does achieving it require?"** Here that question collapses a subarray problem into a run-length problem. It is the same move as asking "what is the maximum achievable profit per day?" in stock problems, or "what is the smallest capacity that could work?" in binary-search-on-answer problems. Bounding the answer first often makes the search trivial.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and)
