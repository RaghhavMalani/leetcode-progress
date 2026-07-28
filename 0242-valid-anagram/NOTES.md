# 242. Valid Anagram
> **Easy** &nbsp;&middot;&nbsp; Hash map · frequency count &nbsp;&middot;&nbsp; family: **Hashing**

Frequency counting in its simplest form. Two things worth stealing: the O(1) length rejection first, and `dict.get(k, 0)` as the idiom for "increment a possibly-missing key".

**▶ [Step through this solution line by line](./visualization.html)** — 17 steps, traced on `s = "anagram", t = "nagaram"`.

| | |
|---|---|
| time | O(n) |
| space | O(alphabet) — O(1) if the alphabet is fixed at 26 |

## The idea

Two strings are anagrams iff their **character multisets** are equal. A dict (or `Counter`, or a 26-slot array) represents a multiset in O(1) per update, so the whole comparison is linear.

## How to recognise it

- Any question about **rearrangement**, "same letters", "permutation of" — the multiset is the invariant.
- Fixed small alphabet → a 26-length list is faster and lighter than a dict, and worth mentioning.
- If you need to find anagrams inside a longer string, this becomes a sliding window over a counter (LC 438).

## Where people go wrong

- **Skipping the length check.** Not just an optimisation: without it, "a" vs "aa" needs the counter comparison to catch it, which it does — but the check documents your thinking and costs nothing.
- **`sorted(s) == sorted(t)`.** Correct and one line, but O(n log n). Fine to offer, then improve.
- **Assuming ASCII lowercase** when the follow-up explicitly asks about Unicode. With Unicode, a dict is required and a 26-slot array is wrong.
- **Comparing `len(dict)` instead of the dicts.** Same number of distinct letters does not mean same counts.

## The reusable template

```python
# Frequency counting - the three idioms worth having in your fingers
count = {}
for c in s:
    count[c] = 1 + count.get(c, 0)      # dict, any alphabet

from collections import Counter
count = Counter(s)                      # same thing, batteries included

count = [0] * 26                        # fixed small alphabet: fastest
for c in s:
    count[ord(c) - ord('a')] += 1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Group all anagrams together | LC 49 — the counter becomes a dictionary key. |
| Find all anagram start indices in a string | LC 438 — fixed-size sliding window over a counter. |
| Anagram after at most one swap | Count positions that differ; must be exactly 0 or 2 and mirror-equal. |
| Unicode input | Dict only. State this before someone asks. |

## How to think about it next time

Easy problems are where you build **idiom fluency**. `d[k] = 1 + d.get(k, 0)`, `Counter(s) == Counter(t)`, `ord(c) - ord('a')` — these should be typing reflexes, not decisions, so that in a hard problem your attention is free for the actual algorithm. When you finish an easy problem, ask "did I write that fluently, or did I have to think?" and drill whatever was slow.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/valid-anagram)
