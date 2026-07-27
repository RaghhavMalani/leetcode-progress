# 3614. Process String With Special Operations II
> **Hard** &nbsp;·&nbsp; Forward lengths + backward index mapping &nbsp;·&nbsp; family: **Math & number theory**

The result can be exponentially long, so you never build it. Instead: track only the LENGTH forwards, then map the query index BACKWARDS through each operation until it lands on a literal character.

**▶ [Step through this solution line by line](../visualizations/3614-process-string-with-special-operations-ii.html)** — 19 steps, traced on `s = "a#b%*", k = 1`.

| | |
|---|---|
| time | O(n) |
| space | O(n) |

## The idea

When a construction is too large to materialise but you only need **one element of it**, run the process forwards to record cheap summary data (here, lengths), then run it backwards translating the query index through each step’s inverse. Doubling inverts to a modulo; reversal inverts to `len − 1 − k`; appending inverts to an equality test.

## How to recognise it

- A described construction whose size grows multiplicatively (doubling, repeating, concatenating with itself) plus a query for a single index.
- The phrase "the string may be very large" or constraints where the output length would overflow.
- The classic family member is LC 880 Decoded String at Index — the same forward-length / backward-index technique.

## Where people go wrong

- **Building the string.** With n operations of "#" the length is 2ⁿ. This is the trap.
- **Overflow in the length.** The forward pass must cap or use big integers; in Python it is free, in C++ you clamp once the length exceeds k.
- **Getting an inverse backwards.** Reversal is `before - 1 - k`, not `before - k`. Doubling is `k % before`, and it needs `before > 0`.
- **Handling "*" as if it shifted indices.** It removes from the END, so surviving indices keep their positions.
- **Forgetting the `k >= final_length` guard** that returns ".".

## The reusable template

```python
"# never build the object - track LENGTHS forward, map the INDEX backward\nlength = [0] * (n + 1)                 # phase 1: forward, cheap summary only\nfor i, ch in enumerate(s):\n    c = length[i]\n    if   ch.isalpha(): c += 1\n    elif ch == '*':    c = max(0, c - 1)\n    elif ch == '#':    c *= 2\n    length[i + 1] = c                  # '%' leaves it unchanged\n\nif k >= length[n]: return '.'\n\nfor i in range(n - 1, -1, -1):         # phase 2: backward, invert each op\n    ch, before = s[i], length[i]\n    if   ch.isalpha() and k == before: return ch        # it IS this letter\n    elif ch == '#' and before:         k %= before      # doubling -> modulo\n    elif ch == '%':                    k = before - 1 - k   # reversal\n    # '*' removed from the END -> surviving indices unaffected\n"
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Decoded String at Index** (LC 880) | The canonical version: repeated concatenation, index mapped back with a modulo. |
| Return a RANGE of characters | Run the backward mapping once per index, or reconstruct only the needed segment. |
| Operations include arbitrary insertion | The inverse gets harder; you may need a rope or a balanced BST. |
| Part I with small constraints | Just simulate the string — which is exactly why Part II exists. |

## How to think about it next time

The reusable idea is **"simulate the metadata, not the object"**. If you only ever need a summary (length, count, k-th element) then carry the summary forward and answer the query by inverting the process. This shows up in string-expansion problems, in fast-exponentiation-style constructions, and in any "the answer is astronomically large but the query is one item" setup. Ask yourself: *what is the smallest thing I can track that still answers the question?*

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii)
