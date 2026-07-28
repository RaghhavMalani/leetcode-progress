# 3. Longest Substring Without Repeating Characters
> **Medium** &nbsp;&middot;&nbsp; Sliding window · variable size &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

The reference implementation for variable-size sliding windows. Grow on the right, shrink on the left until the window is legal again, record. Neither pointer ever goes backwards.

**▶ [Step through this solution line by line](./visualization.html)** — 40 steps, traced on `s = "abcabcbb"`.

| | |
|---|---|
| time | O(n) — l and r each advance at most n times |
| space | O(min(n, alphabet)) |

## The idea

A sliding window is two pointers that **only ever move right**. The outer loop grows the window; an inner `while` shrinks it back to legality. Because neither pointer rewinds, the inner loop is not a nested O(n) — the total work is amortised to 2n. If you ever find yourself resetting `l` back to `r`, or restarting a scan, you have left the pattern and gone quadratic.

## How to recognise it

- **Contiguous** subarray or substring — the word "substring" or "subarray" (not "subsequence") is the single strongest signal.
- Asking for the **longest / shortest / count** of stretches satisfying some property.
- The property is **monotone**: if a window is invalid, growing it right cannot fix it — only shrinking from the left can. That is what licenses the pattern.
- Contrast: "subsequence" means elements need not be adjacent, which kills sliding window and usually means DP.

## Where people go wrong

- **`s1.remove(s[r])` instead of `s1.remove(s[l])`.** You must evict from the left edge, not the character that caused the collision.
- **Using `if` instead of `while`.** One eviction is not always enough — you shrink until the window is legal, however many steps that takes.
- **Recording the answer inside the while loop.** Measure only after the window is valid again.
- **Off-by-one in the length.** An inclusive window s[l..r] has length `r - l + 1`. Write it out rather than trusting instinct.
- **Jumping `l` straight past the duplicate** using a last-seen map is a valid faster variant — but then you must guard `l = max(l, last[c] + 1)`, or a stale index drags l backwards.

## The reusable template

```python
# Variable-size sliding window - the universal shape
left = 0
for right in range(len(s)):
    add(s[right])                       # 1. grow

    while window_is_invalid():          # 2. shrink until legal again
        remove(s[left])
        left += 1

    ans = best(ans, right - left + 1)   # 3. record

# "Count substrings" variant: when the window at `right` is the SMALLEST
# valid one, every extension of it is also valid, so add (n - right).
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| At most k distinct characters | LC 340 — swap the set for a counter, invalid when `len(counter) > k`. |
| Longest repeating character replacement | LC 424 — invalid when `window_len - max_freq > k`. |
| **Minimum** window substring | LC 76 — record inside the shrink loop instead of after it; you want the smallest valid window, not the largest. |
| Fixed-size window of length k | No while loop at all — add s[r], remove s[r-k], record. Strictly simpler. |
| Count substrings with the property | LC 1358 — add `n - right` per valid window. See that page. |

## How to think about it next time

Every sliding-window problem is three questions. **(1) What makes a window invalid?** Here: a repeated character. **(2) What do I do to fix it?** Evict from the left. **(3) When do I record?** After it is valid, if I want the longest; during the shrink, if I want the shortest. Answer those three in English before writing a line, and the code writes itself. If you cannot answer (2) — if shrinking from the left does not obviously restore legality — the problem is probably not a sliding window at all.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters)
