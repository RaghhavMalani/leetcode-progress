# 1448. Maximum 69 Number
> **Easy** &nbsp;&middot;&nbsp; Greedy · positional value &nbsp;&middot;&nbsp; family: **Greedy**

Three lines, and the argument behind them is worth more than the code: a digit change at place 10^k is worth 3·10^k, so always change the leftmost 6.

**▶ [Step through this solution line by line](./visualization.html)** — 4 steps, traced on `num = 9669`.

| | |
|---|---|
| time | O(d) in the number of digits |
| space | O(d) |

## The idea

In a positional number system, a change to a more significant digit dominates **any** combination of changes to less significant ones. That is why greedy-from-the-left is correct for essentially every "maximise/minimise the number by editing digits" problem.

## How to recognise it

- "Change at most k digits to maximise/minimise the number."
- Maximising → change the leftmost improvable digit. Minimising → same idea, opposite direction, with the extra rule that a leading digit usually cannot become 0.
- `str.replace(old, new, 1)` — that third argument is the whole solution and most people do not know it exists.

## Where people go wrong

- **Replacing all 6s.** The problem allows exactly one change. Forgetting the count argument is the bug.
- **Changing the last 6.** Correct code, wrong digit, much smaller answer.
- **Special-casing "no 6 present".** Unnecessary — `replace` returns the string unchanged.
- **Forgetting the `int()` conversion back.** The function must return a number.

## The reusable template

```python
# positional dominance: a change at 10^k beats everything to its right
return int(str(num).replace('6', '9', 1))    # the 1 = "first occurrence only"

# at most k changes:      str(num).replace('6', '9', k)
# minimising instead:     change the leftmost 9 -> 6 (mind leading zeros)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Change at most k digits | Replace the k leftmost 6s: `s.replace("6","9",k)`. |
| **Minimise** the number | Change the leftmost 9 to 6 — but if it is the leading digit and the target is 0, skip it. |
| **Remove K Digits** (LC 402) | Now greedy needs a monotonic stack, because removals interact. |
| **Maximum Swap** (LC 670) | Swap two digits — greedy needs the last occurrence of each larger digit. |

## How to think about it next time

For any digit-editing problem, ask **"what is the marginal value of a change at position k?"** In base 10 it is proportional to 10^k, which decays fast enough that the leftmost improvable position always wins. Once a problem lets changes *interact* — removals shifting digits, swaps — that simple dominance breaks and you need a stack or a full case analysis. Knowing which regime you are in is the whole skill.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/maximum-69-number)
