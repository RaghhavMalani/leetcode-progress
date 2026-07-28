# 288. Unique Word Abbreviation
> **Medium** &nbsp;&middot;&nbsp; Design · precompute a canonical key &nbsp;&middot;&nbsp; family: **Hashing**

A canonical-key problem (like LC 49) turned into a data structure. The neat move is the `""` sentinel: instead of storing a set of words per abbreviation, one poisoned entry says "contested".

**▶ [Step through this solution line by line](./visualization.html)** — 15 steps, traced on `dictionary = ["deer","door","cake","card"], then four isUnique queries`.

| | |
|---|---|
| time | O(total characters) to build, O(1) per query |
| space | O(number of distinct abbreviations) |

## The idea

Precompute so that queries are trivial. And note the space optimisation: you do not need the *set* of words behind each abbreviation — only "exactly one word, and here it is" or "more than one". Collapsing a set into a two-state value is a small idea that shows up constantly in real systems.

## How to recognise it

- A structure built once and queried many times — the cost model rewards precomputation heavily.
- "Unique" defined against a fixed reference collection.
- The abbreviation function is a canonical key, exactly as in LC 49 group anagrams.

## Where people go wrong

- **Missing the "same word" case.** If the dictionary contains "deer" twice, "deer" is still unique. Line 12 exists for this and it is the case that fails most submissions.
- **Words of length ≤ 2.** "it" abbreviated by the formula would be "i0t", which is longer than the word. The guard returns the word itself.
- **Storing full sets of words.** Correct but wasteful; the "" sentinel captures everything you need.
- **Using `None` as the sentinel instead of `""`.** Also fine — just make sure the sentinel can never be a real word.

## The reusable template

```python
# Precompute a canonical key; collapse "a set of things" into a flag
abbr_map = {}
for word in dictionary:
    a = abbr(word)
    if a not in abbr_map:
        abbr_map[a] = word        # exactly one owner so far
    elif abbr_map[a] != word:
        abbr_map[a] = ""          # contested - sentinel no real word can equal

def isUnique(word):
    a = abbr(word)
    return a not in abbr_map or abbr_map[a] == word

def abbr(w):
    return w if len(w) <= 2 else w[0] + str(len(w) - 2) + w[-1]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Generalized Abbreviation** (LC 320) | Generate all abbreviations of a word — backtracking, take/skip per character. |
| **Valid Word Abbreviation** (LC 408) | Verify one abbreviation against one word — a two-pointer parse. |
| **Word Abbreviation** (LC 527) | Find the shortest unambiguous abbreviation for every word. This problem, escalated. |
| Queries can add words | You would need the real set per abbreviation, since removals could un-contest one. |

## How to think about it next time

Two habits from this problem. First: when a structure is **built once and queried many times**, push all the work into construction — that asymmetry is usually the point. Second: before storing a collection per key, ask **what you actually need to know about it**. Here it is only "one or many", which is two states, not a set. That kind of compression is what separates a solution that fits in memory from one that does not.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/unique-word-abbreviation)
