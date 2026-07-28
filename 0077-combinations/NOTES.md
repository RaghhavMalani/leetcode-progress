# 77. Combinations
> **Medium** &nbsp;&middot;&nbsp; Backtracking · loop form &nbsp;&middot;&nbsp; family: **Backtracking**

The same pattern in its other dialect: one `for` loop with one recursive call, instead of two explicit branches. Passing `i+1` as the next start is what forces combinations to increase.

**▶ [Step through this solution line by line](./visualization.html)** — 46 steps, traced on `n = 4, k = 2`.

| | |
|---|---|
| time | O(C(n,k) · k) |
| space | O(k) depth |

## The idea

Backtracking comes in two dialects and they are fully interchangeable. **Take/skip** (problems 39, 78, 90) makes one binary decision per element. **Loop form** (this problem, 46, 47) iterates over all choices available at this level. Loop form is shorter when the number of choices per level varies; take/skip is clearer when each element has exactly two fates.

## How to recognise it

- "Choose k of n, order irrelevant" — the definition of a combination.
- The answer set has size C(n,k), which is small for the given constraints (n ≤ 20, k ≤ n).
- Whenever output must be non-decreasing / non-repeating in position, the fix is **recurse from i+1, not from start**.

## Where people go wrong

- **`backtrack(start+1, …)` instead of `backtrack(i+1, …)`.** A subtle and very common slip: it lets you revisit values and produces permutations, not combinations.
- **`backtrack(i, …)`** allows reuse — that would be LC 39 with a length target instead of a sum target.
- **Missing the `.copy()`.** Same story as always.
- **No early cut.** If `n - i + 1 < k - len(comb)` there are not enough numbers left to ever finish; `break` there and the dead-end branch you can see in this trace disappears.

## The reusable template

```python
def backtrack(state):
    if is_complete(state):
        res.append(path.copy())
        return
    if is_impossible(state):
        return
    for choice in choices(state):
        path.append(choice)          # choose
        backtrack(advance(state))    # explore
        path.pop()                   # un-choose
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Sum to n using k digits 1..9 | LC 216 — same loop, add a running total and two guards. |
| All subsets (any k) | LC 78 — save at *every* node instead of only at depth k, or loop k from 0 to n. |
| Combinations with repetition allowed | Recurse from `i` instead of `i+1`. |
| Just the count | C(n,k) — Pascal or a factorial formula. No search. |

## How to think about it next time

Practise converting between the two dialects. Take your problem 78 solution and rewrite it as a loop; take this one and rewrite it as take/skip. Ten minutes of that does more for your fluency than five new problems, because after it you stop seeing "combination problems" and "subset problems" as different — they are the same tree with a different rule for when you save.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/combinations)
