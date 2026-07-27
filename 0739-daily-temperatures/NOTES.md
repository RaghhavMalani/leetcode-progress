# 739. Daily Temperatures
> **Medium** &nbsp;·&nbsp; Monotonic stack · next greater element &nbsp;·&nbsp; family: **Stacks & monotonic stacks**

The canonical monotonic stack. Every index is pushed once and popped once, so the nested while loop is still O(n) — the same amortised argument as LC 128.

**▶ [Step through this solution line by line](../visualizations/0739-daily-temperatures.html)** — 28 steps, traced on `temperatures = [73,74,75,71,69,72,76,73]`.

| | |
|---|---|
| time | O(n) amortised — n pushes, at most n pops |
| space | O(n) |

## The idea

A **monotonic stack** holds items still waiting for an answer, kept in sorted order. When a new item arrives it resolves — and pops — everything it dominates. The stack is decreasing here because we are looking for the *next greater* element; flip the comparison for next-smaller.

## How to recognise it

- "**Next greater / next smaller / previous greater / previous smaller**" element, or "how long until…". This exact phrasing is the pattern’s signature.
- The brute force is an O(n²) double loop and the constraints forbid it.
- Also: largest rectangle in a histogram, stock spans, trapping rain water, and remove-k-digits — all the same stack with different bookkeeping.

## Where people go wrong

- **Storing values instead of indices.** You need the index to compute the distance. Store indices, look up values.
- **`>=` instead of `>`.** Decides how equal temperatures behave. Here the question says strictly warmer, so `>`. Get this wrong and duplicates break silently.
- **Believing the while loop makes it O(n²).** It does not — each index enters and leaves the stack exactly once. Be ready to say that; it is the question that follows.
- **Forgetting the leftovers.** Indices still on the stack at the end have no answer; pre-filling with 0 handles it, but say so rather than leaving it to luck.

## The reusable template

```python
# Monotonic stack - "next greater element", O(n) amortised
stack = []                      # holds INDICES, kept decreasing by value
ans = [0] * n
for i, x in enumerate(a):
    while stack and x > a[stack[-1]]:      # x resolves everything it dominates
        j = stack.pop()
        ans[j] = i - j                     # or a[i], or an area, ...
    stack.append(i)
# leftovers on the stack have no answer -> keep the default

# next SMALLER element: flip to  while stack and x < a[stack[-1]]
# previous greater:     read stack[-1] BEFORE you push
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Next Greater Element I / II** (LC 496 / 503) | Same stack; for the circular version, loop over the array twice. |
| **Largest Rectangle in Histogram** (LC 84) | Increasing stack; on pop you compute an area. The hardest member of the family. |
| **Trapping Rain Water** (LC 42) | Solvable with this stack layer by layer — your repo uses the two-pointer version, which is better. |
| **Remove K Digits** / smallest subsequence (LC 402 / 1081) | Increasing stack with a pop budget. Your repo has LC 1081. |
| Previous smaller element | Same loop, comparison flipped, and you read the stack top before pushing. |

## How to think about it next time

The mental model that makes monotonic stacks click: **the stack is a queue of unanswered questions, kept sorted so that one new fact answers a whole prefix of them at once.** When you meet a problem where each element needs to look forward for "the first thing bigger/smaller than me", do not write the double loop — ask what order the pending elements would naturally be in, and you will find the stack is already monotone.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/daily-temperatures)
