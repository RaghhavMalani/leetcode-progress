# 1967. Number of Strings That Appear as Substrings in Word
> **Easy** &nbsp;&middot;&nbsp; String matching · know what your library does &nbsp;&middot;&nbsp; family: **Brute force done right**

Three lines. Worth a minute anyway, because it is a good moment to know what `in` actually costs and what you would reach for if the input were a million times bigger.

**▶ [Step through this solution line by line](./visualization.html)** — 10 steps, traced on `patterns = ["a","abc","bc","d"], word = "abc"`.

| | |
|---|---|
| time | O(Σ|p| × |word|) worst case with naive matching; CPython uses a Crochemore–Perrin variant that is near-linear in practice |
| space | O(1) |

## The idea

Use the built-in when the constraints allow it, and be able to say what you would use if they did not. The escalation ladder for substring search is: **naive** O(nm) → **KMP / Z-algorithm** O(n+m) for one pattern → **Aho–Corasick** O(n + Σm + matches) for many patterns at once → **suffix automaton / suffix array** when the text is fixed and queried repeatedly.

## How to recognise it

- "Does A appear inside B" with small inputs → just use `in`.
- Many patterns against one text → Aho–Corasick builds a trie with failure links and scans the text once.
- One fixed text, many queries → build a suffix structure over the text instead.

## Where people go wrong

- **Writing your own matcher unprompted.** With n ≤ 100 it is noise. Use the library and mention the alternative.
- **Confusing substring with subsequence.** Substring is contiguous; subsequence is not. `in` tests substrings only.
- **Assuming `in` is O(n).** It is not guaranteed to be, and in a language like C++ `find` is genuinely O(nm) in the worst case.

## The reusable template

```python
count = sum(1 for p in patterns if p in word)

# escalation ladder when the constraints grow:
#   one pattern, big text     -> KMP / Z-algorithm      O(n + m)
#   MANY patterns, one text   -> Aho-Corasick           O(n + sum(m) + hits)
#   one fixed text, many queries -> suffix automaton / suffix array
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Count occurrences, not just presence | `word.count(p)` — but note it counts NON-overlapping occurrences. |
| Many patterns, huge text | Aho–Corasick. One pass over the text finds all patterns. |
| Subsequence instead of substring | LC 392 — a two-pointer greedy walk. |
| **Find the index** of the first occurrence (LC 28) | The classic KMP exercise. |

## How to think about it next time

For every library call you make in an interview, be ready to answer **"what does that do under the hood, and what is its complexity?"** You will almost never need to implement it — but the follow-up "now the text is 10⁹ characters and you have 10⁵ patterns" is exactly where a candidate either names Aho–Corasick or goes quiet. Knowing the escalation ladder is cheap insurance.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word)
