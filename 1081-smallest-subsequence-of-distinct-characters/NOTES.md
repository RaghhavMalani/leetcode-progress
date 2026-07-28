# 1081. Smallest Subsequence of Distinct Characters
> **Medium** &nbsp;&middot;&nbsp; Monotonic stack · greedy with a safety check &nbsp;&middot;&nbsp; family: **Stacks & monotonic stacks**

A monotonic stack with one extra condition. Popping a bigger character is only safe if it *reappears later* — the `last` array is what makes the greedy legal.

**▶ [Step through this solution line by line](./visualization.html)** — 20 steps, traced on `s = "cbacdcbc"`.

| | |
|---|---|
| time | O(n) amortised — each character pushed once, popped once |
| space | O(alphabet) |

## The idea

Lexicographic minimisation with a monotonic stack. The greedy rule is: **if the character on top of the stack is larger than the incoming one, drop it** — but only when you can afford to, meaning it occurs again later. That safety condition is the difference between this and the plain "next smaller element" stack.

## How to recognise it

- "Lexicographically smallest / largest result after removing or reordering characters."
- The pair of conditions "top > current" (greedy improvement) and "top occurs again" (feasibility) is the fingerprint of this family.
- Same skeleton as LC 402 Remove K Digits, where the feasibility condition is a removal budget instead of a future occurrence.

## Where people go wrong

- **Dropping the `last[...] > i` check.** You lose characters permanently and the result is missing letters.
- **Forgetting to un-mark `used` when popping.** The character can never be re-added and the answer is short.
- **Not skipping characters already in the result.** Duplicates appear.
- **Believing the while loop makes it O(n²).** It does not — the standard amortised argument, same as LC 739 in your repo.
- **Using a count-remaining array instead of last-index.** Both work; be consistent, because mixing them breaks the condition.

## The reusable template

```python
# monotonic stack + FEASIBILITY check
last = {c: i for i, c in enumerate(s)}     # last occurrence of each character
stack, used = [], set()

for i, c in enumerate(s):
    if c in used:                           # each letter appears exactly once
        continue
    while stack and stack[-1] > c and last[stack[-1]] > i:
        #        greedy improvement ^^^        ^^^ safe: it comes again
        used.discard(stack.pop())
    stack.append(c); used.add(c)

return "".join(stack)
# LC 402 is the same loop with "while k > 0" as the feasibility condition.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Remove K Digits** (LC 402) | Pop while the top is larger AND you still have removals left. Same stack, budget instead of last-index. |
| **Remove Duplicate Letters** (LC 316) | Literally the same problem under a different number. |
| Lexicographically LARGEST | Flip the comparison to `top < current`. |
| **Create Maximum Number** (LC 321) | This greedy applied twice, plus a merge. Genuinely hard. |

## How to think about it next time

Greedy plus a feasibility check is a recurring shape: **"take the locally best action, but only if it does not make the goal unreachable."** Here the goal is "every distinct letter must appear", and the check is "this letter comes again". In Remove K Digits the goal is "remove exactly k" and the check is the remaining budget. When you meet a lexicographic-optimisation problem, ask those two questions separately — what is the greedy improvement, and what makes it safe — and the code writes itself.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters)
