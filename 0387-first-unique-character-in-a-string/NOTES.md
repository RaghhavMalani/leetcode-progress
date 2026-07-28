# 387. First Unique Character in a String
> **Easy** &nbsp;&middot;&nbsp; Hash map · two-pass frequency &nbsp;&middot;&nbsp; family: **Hashing**

The "two passes are fine" lesson. You cannot answer this in one pass because uniqueness is only known after seeing the whole string — and iterating the *string* in pass two, not the dictionary, is what makes "first" correct.

**▶ [Step through this solution line by line](./visualization.html)** — 18 steps, traced on `s = "loveleetcode"`.

| | |
|---|---|
| time | O(n) — two passes is still linear |
| space | O(1) — at most 26 keys |

## The idea

Some properties are only decidable once you have seen everything ("is this unique?"), while the question asks for the earliest occurrence. The resolution is **gather in pass one, decide in pass two**. Do not contort yourself trying to do it in one pass; two linear passes are still linear.

## How to recognise it

- "First / leftmost X such that some GLOBAL property holds." The global property forces a first pass.
- Frequency-of-characters problems generally: count first, then act.
- If you truly need one pass over a stream, you need a different structure entirely — an ordered dict or a queue of candidates.

## Where people go wrong

- **Iterating `count` instead of `s` in pass two.** In modern Python dicts preserve insertion order so it happens to work — but it is accidental, and it breaks the moment you use a `set` or another language. Iterate the string.
- **`s.index(ch)` inside a loop** — each call is O(n), so the whole thing becomes O(n²).
- **Forgetting to return −1.** "aabb" has no answer.
- **Claiming O(n) space.** With a fixed 26-letter alphabet it is O(1), and saying so is free credit.

## The reusable template

```python
# Gather, then decide
count = Counter(s)                  # pass 1: global information
for i, ch in enumerate(s):          # pass 2: iterate the INPUT to keep order
    if count[ch] == 1:
        return i
return -1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| First unique in a **stream** | LC 387 follow-up — a queue of candidates plus a count map, popping stale heads. |
| First **repeating** character | One pass with a set — repetition IS decidable early, which is why this one is easier. |
| Last unique character | Same two passes, walk pass two backwards. |
| **Sort characters by frequency** (LC 451) | Count, then sort the items by count. Same first pass. |

## How to think about it next time

When a one-pass solution feels impossible, ask **"is this property decidable from a prefix?"** Repetition is (you know the moment you see it twice). Uniqueness is not (you only know at the end). If the answer is no, stop fighting and take the second pass — candidates rejected for being "inelegant" are usually just correct. The genuinely one-pass version of this problem requires a queue, which is more machinery, not less.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string)
