# 49. Group Anagrams
> **Medium** &nbsp;&middot;&nbsp; Hash map · canonical key &nbsp;&middot;&nbsp; family: **Hashing**

Grouping by a *canonical form*. The counting signature is O(n·k) where sorting each word would be O(n·k log k) — a small but real win, and the version worth knowing.

**▶ [Step through this solution line by line](./visualization.html)** — 38 steps, traced on `strs = ["eat","tea","tan","ate","nat","bat"]`.

| | |
|---|---|
| time | O(n · k) where k is the average word length — beats sort-based O(n · k log k) |
| space | O(n · k) |

## The idea

To group things that are "the same up to some transformation", invent a **canonical key**: a value that is identical for everything in a group and unique across groups. Then one pass with a dictionary does all the grouping. The art is picking a key that is cheap to compute and cannot collide.

## How to recognise it

- "Group / bucket / partition these by some equivalence" — anagrams, isomorphic strings, similar shapes, congruent islands.
- The naive approach is comparing every pair (O(n²) comparisons). A canonical key removes the pairwise comparison entirely.
- Look for the cheapest invariant: for anagrams it is the letter multiset; for isomorphic strings it is the pattern of first occurrences; for island shapes it is the normalised set of relative coordinates.

## Where people go wrong

- **Using a list as a dict key.** `hashmap[count]` raises `TypeError: unhashable`. `tuple(count)` is the fix and this is the line people forget.
- **Reusing the counter across words.** It must be reset inside the loop — line 7 is inside the `for` for a reason.
- **Assuming lowercase ASCII.** `ord(char) - ord('a')` goes negative on uppercase or Unicode. Fine here because the constraints say lowercase; say so aloud rather than leaving it implicit.
- **Sorting each word.** Perfectly acceptable and shorter (`tuple(sorted(w))`) — but mention that counting is asymptotically better when words are long.

## The reusable template

```python
# Group by canonical key - one pass, no pairwise comparison
groups = defaultdict(list)
for item in items:
    groups[canonical(item)].append(item)     # key MUST be hashable
return list(groups.values())

# anagrams:          tuple(counts_of_26)   or  tuple(sorted(word))
# isomorphic:        tuple(first_seen_index_of_each_char)
# island shapes:     tuple(coords normalised to the top-left cell)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Isomorphic strings | LC 205 — the key is the sequence of first-occurrence indices. |
| **Number of Distinct Islands** (LC 694) | The key is the shape normalised to the top-left corner. |
| Group by sorted digits, very long words | Counting beats sorting by a bigger margin; with a huge alphabet, hash the counter instead of materialising 26 slots. |
| Anagram check for two strings only | LC 242 — no grouping, just compare two counters. |

## How to think about it next time

Any time a problem says "these two things count as the same", the question to ask is **"what is the smallest piece of data that decides sameness?"** That is your key. Compute it once per item, dictionary-group, done. This reflex turns a surprising number of Medium problems into five lines — and when the key is expensive or hard to define, that difficulty *is* the problem, which tells you where to spend your thinking time.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/group-anagrams)
