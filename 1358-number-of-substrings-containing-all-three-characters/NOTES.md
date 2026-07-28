# 1358. Number of Substrings Containing All Three Characters
> **Medium** &nbsp;&middot;&nbsp; Sliding window · counting &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

The counting variant of the sliding window. The whole problem is one line: `ans += n - right`. Understanding *why* that counts each substring exactly once is the skill being tested.

**▶ [Step through this solution line by line](./visualization.html)** — 26 steps, traced on `s = "abcabc"`.

| | |
|---|---|
| time | O(n) — each pointer moves forward at most n times |
| space | O(1) — three counters |

## The idea

When a window is valid, **every extension of it is also valid**. So instead of counting substrings one at a time, find the boundary and count a whole batch. Here, once s[left..right] is valid, so is s[left..right+1] through s[left..n-1] — that is `n - right` substrings, added in O(1).

## How to recognise it

- "Count the number of substrings/subarrays such that …" — count, not longest.
- The property is **monotone under extension**: adding more characters can never break it. "Contains all of X" is monotone; "contains exactly k distinct" is NOT, which is why that problem needs the atMost(k) − atMost(k-1) trick instead.
- n up to 10⁵ — the O(n²) enumeration is being ruled out on purpose.

## Where people go wrong

- **Adding `left + 1` instead of `n - right`.** Both are valid counting schemes but they answer different questions: `n - right` counts by *extending the right end*, `left+1` (used after the shrink loop) counts by *choosing any left start*. Mixing them double-counts.
- **Counting after the while loop instead of inside it.** You would miss every valid window except the last one at each right.
- **Using `if` not `while`.** Several lefts may be valid for the same right.
- **Reaching for this template when the property is not monotone.** "Exactly k distinct" needs `atMost(k) - atMost(k-1)`; applying this one directly gives nonsense.

## The reusable template

```python
# Counting valid windows in O(n)
left, ans = 0, 0
for right in range(n):
    add(s[right])
    while window_is_valid():         # find the smallest valid window
        ans += n - right             # ...and every extension of it
        remove(s[left]); left += 1

# Non-monotone property ("exactly k")? Decompose it:
#   exactly(k) = atMost(k) - atMost(k - 1)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Subarrays with at most k distinct | LC 340 / 992 — same loop, count `right - left + 1` after shrinking. |
| Subarrays with **exactly** k distinct | LC 992 — `atMost(k) - atMost(k-1)`. The single most useful counting trick in this family. |
| Subarrays with product less than k | LC 713 — identical structure, multiply/divide instead of counters. |
| **Longest** substring with all three | Not a count — record `right - left + 1` and take the max. |

## How to think about it next time

Train yourself to spot the sentence **"if this window works, every bigger one works too"**. The moment it is true, counting problems collapse from O(n²) enumeration to O(n) batch counting. And when it is false — "exactly k", "at least k occurrences of the max" — reach for the `atMost(k) − atMost(k−1)` decomposition, which turns a non-monotone question into two monotone ones. Those two ideas cover almost every "count the subarrays" problem you will be asked.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters)
