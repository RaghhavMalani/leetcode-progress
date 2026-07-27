# 14. Longest Common Prefix
> **Easy** &nbsp;·&nbsp; Vertical scanning &nbsp;·&nbsp; family: **Two pointers & sliding window**

Vertical scanning: compare position 0 across all words, then position 1, and stop at the first disagreement. Better than the horizontal version because it exits early on the most common inputs.

**▶ [Step through this solution line by line](../visualizations/0014-longest-common-prefix.html)** — 18 steps, traced on `strs = ["flower","flow","flight"]`.

| | |
|---|---|
| time | O(S) worst case where S is the total number of characters; O(n · answer length) in practice |
| space | O(1) |

## The idea

Two ways to scan. **Horizontal:** fold the prefix across words one at a time (prefix = LCP(prefix, next)). **Vertical (this code):** fix a column and check it across every word. Vertical is better when the answer is short, because it stops after examining only `answer_length × n` characters instead of reading a long first word in full.

## How to recognise it

- "Common prefix / suffix / shared start" across a collection.
- The answer is bounded by the shortest string — a useful early observation, and it gives an O(n log n) binary-search variant.
- If prefixes are queried repeatedly against a growing set, build a **trie** instead: the LCP is the path down to the first branching node.

## Where people go wrong

- **Checking `other[i] != char` before the length check.** IndexError on "flow" at i = 4. The `or` short-circuits in the right order here — that ordering is the bug most people write.
- **Empty input.** `strs[0]` would raise. Line 7 handles it.
- **An empty string in the list.** The answer is "" immediately, and the length check catches it on the first iteration.
- **Sorting the array and comparing only first and last.** Clever and correct (the extremes bound everything between) — but O(n log n · m) and worth mentioning only as a curiosity.

## The reusable template

```python
# vertical scanning - exits at the first disagreement
if not strs:
    return ""
for i, ch in enumerate(strs[0]):
    for other in strs[1:]:
        if i >= len(other) or other[i] != ch:   # LENGTH CHECK FIRST
            return strs[0][:i]
return strs[0]

# horizontal alternative: fold  prefix = lcp(prefix, word)  over the list
# many queries over a growing set: build a trie instead
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Longest common SUFFIX | Reverse everything and run the same code. |
| LCP of two strings only | A single while loop. |
| Many prefix queries over a set | Build a trie; the LCP is the path to the first node with more than one child. |
| **Longest common SUBSTRING** (not prefix) | A completely different problem — DP or suffix automaton. |

## How to think about it next time

When you have a choice of scan direction, ask **which one exits earliest on realistic input**. Vertical scanning wins here because common prefixes are usually short. The same reasoning shows up everywhere: check the cheap disqualifying condition first, iterate over the smaller collection in a nested loop, and order your `or` conditions so the safe check short-circuits the dangerous one — which is literally what line 12 is doing.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/longest-common-prefix)
