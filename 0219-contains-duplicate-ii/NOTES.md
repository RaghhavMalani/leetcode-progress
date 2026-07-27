# 219. Contains Duplicate II
> **Easy** &nbsp;·&nbsp; Sliding window · fixed size &nbsp;·&nbsp; family: **Two pointers & sliding window**

A fixed-size window instead of a variable one — no `while` loop, just "add one, drop one". The trick is realising that "indices at most k apart" IS a window of size k+1.

**▶ [Step through this solution line by line](../visualizations/0219-contains-duplicate-ii.html)** — 20 steps, traced on `nums = [1,2,3,1,2,3], k = 2`.

| | |
|---|---|
| time | O(n) |
| space | O(min(n, k)) |

## The idea

Two window flavours. **Variable size** (LC 3, 1358): grow right, shrink left with a `while` until legal. **Fixed size** (this one): the window is always the same width, so eviction is a single `if`, not a loop. Recognising which flavour you need before you start saves you from writing a while loop that never runs.

## How to recognise it

- A constraint on the **distance between indices** — "at most k apart", "within k positions" — is a fixed window in disguise.
- Any "last k elements" phrasing: running average of the last k, max of the last k, and so on.
- If the width depends on the data rather than a given constant, you need the variable-size version instead.

## Where people go wrong

- **Window of size k instead of k+1.** Indices i and j with `|i-j| ≤ k` means k+1 slots. The condition `R - L > k` encodes that correctly; `>= k` would be off by one and miss the boundary case.
- **Checking membership before evicting.** A stale element still in the set produces a false positive. Evict first, then test.
- **Using a dict of last-seen index instead of a set.** Also correct (`if x in last and R - last[x] <= k`) and arguably clearer — but then you must not evict, since the dict holds the whole history.
- **The O(n·k) double loop.** Passes the easy tests, times out on the real constraints.

## The reusable template

```python
# Fixed-size window - add one, drop one, no while loop
window = set()          # or a deque / counter / running sum
left = 0
for right in range(len(a)):
    if right - left > k:            # too wide by exactly one
        window.remove(a[left]); left += 1
    if a[right] in window:
        return True
    window.add(a[right])
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Values within t AND indices within k | LC 220 — needs a sorted window (bucketing or a balanced BST), not a plain set. |
| Any duplicate anywhere | LC 217 — `len(set(nums)) != len(nums)`, no window at all. |
| Max of every window of size k | LC 239 — a monotonic deque, the classic upgrade from set to deque. |
| Longest window with a property | Variable size — see LC 3. |

## How to think about it next time

When a problem constrains **index distance**, translate it immediately into a window width and write that width down. "At most k apart" → width k+1. "Exactly k apart" → not a window, just direct indexing. Getting this translation on paper first eliminates the entire class of off-by-one bugs that make these easy problems embarrassing.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/contains-duplicate-ii)
