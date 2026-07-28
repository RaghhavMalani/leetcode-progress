# 78. Subsets
> **Medium** &nbsp;&middot;&nbsp; Backtracking · take / skip &nbsp;&middot;&nbsp; family: **Backtracking**

The cleanest specimen in the whole family. Take or skip, once per element, three levels deep, 2³ leaves and every one is an answer. If the choose/explore/un-choose rhythm ever stops making sense, come back to this page.

**▶ [Step through this solution line by line](./visualization.html)** — 54 steps, traced on `nums = [1,2,3]`.

| | |
|---|---|
| time | O(2ⁿ · n) — 2ⁿ subsets, n to copy each |
| space | O(n) depth |

## The idea

Every subset is a length-n string of yes/no decisions. That is literally what the recursion tree draws: level i decides element i, so a root-to-leaf path *is* a binary string, and there are 2ⁿ of them. Understanding this one bijection makes the bitmask solution obvious too.

## How to recognise it

- "All subsets", "the power set", "every possible selection" with n ≤ 20 or so.
- No constraint linking the elements — each decision is independent. That independence is why there are no dead ends here and plenty in problem 39.
- A count-only version would be trivially 2ⁿ, so if the problem asks for a count it is almost certainly asking something harder than it looks.

## Where people go wrong

- **Saving only at the leaves vs at every node.** Both work for subsets, but they save *different things*: this version saves at leaves after all n decisions; the loop-form version saves at every node. Mixing the two idioms half-way produces duplicates.
- **Forgetting `.copy()`** — here it genuinely bites, unlike in problem 22.
- **Believing you need to sort.** You do not, unless there are duplicates (that is LC 90).

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
| Input has duplicates | LC 90 — sort, then skip equal neighbours on the skip branch. |
| Subsets of exactly size k | LC 77 — add a length guard, or use the loop form. |
| Bitmask instead of recursion | `for mask in range(1<<n)`, include j when `mask & (1<<j)`. Same 2ⁿ work, no call stack, and often the cleanest answer to state in an interview. |
| Sum over all subsets | LC 1863 — usually a bit trick, not enumeration. Each bit is set in exactly half the subsets. |

## How to think about it next time

Use this problem as your reference implementation. When a harder backtracking problem confuses you, ask **"what is different from subsets?"** — usually the answer is one of exactly three things: (1) an extra guard that prunes branches, (2) a rule that suppresses duplicate answers, or (3) a different rule for when you save. Naming which of the three you are dealing with usually writes the code for you.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/subsets)
