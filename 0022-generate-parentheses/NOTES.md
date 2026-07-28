# 22. Generate Parentheses
> **Medium** &nbsp;&middot;&nbsp; Backtracking · build-and-undo &nbsp;&middot;&nbsp; family: **Backtracking**

The cleanest example of *perfect pruning* you will meet. The two guards make an invalid string impossible to construct, so every leaf of the recursion tree is an answer and no work is ever wasted.

**▶ [Step through this solution line by line](./visualization.html)** — 76 steps, traced on `n = 3`.

| | |
|---|---|
| time | O(4ⁿ / √n) — the nth Catalan number, times O(n) to join each string |
| space | O(n) recursion depth + O(n) for the stack (output not counted) |

## The idea

Backtracking is one mechanic wearing different costumes: **choose → explore → un-choose**. A single shared mutable list is threaded through the whole recursion. You push a choice, recurse, then pop it so the next branch starts from a clean state. Everything else — the guards, the loops, the base case — is problem-specific dressing on that skeleton.

## How to recognise it

- The question asks for **all** of something (all strings, all combinations, all paths) rather than a count or a best value. If it asked only for the count, you would reach for DP instead.
- The output size is exponential, and the constraints are tiny to match (`n ≤ 8` here). Small constraints are the interviewer telling you exponential search is acceptable.
- Each answer is built by a **sequence of decisions**, and a partial answer can be extended or abandoned.
- A valid answer has a **local rule** you can check while building — here: never close more than you opened, never open more than n.

## Where people go wrong

- **Appending the list itself instead of a copy.** `res.append(path)` stores a reference; the next `pop()` silently corrupts the answer you just saved. Here `"".join(stack)` happens to build a new string, so this bug hides — in 39, 77 and 78 you must write `.copy()` explicitly.
- **Forgetting the pop.** The branch below inherits a polluted state and you get garbage that is hard to debug because the code still "looks right".
- **Validating at the leaf instead of at the branch.** Generating all 2^(2n) strings and filtering the balanced ones is correct but astronomically slower. Push the check up into the guard.
- **Writing `closeN < n` instead of `closeN < openN`.** That single change lets ")(" through. The guard is not about the budget, it is about what is currently unmatched.

## The reusable template

```python
# The backtracking skeleton. Every problem in this family is this
# shape with different guards.

def backtrack(state):
    if is_complete(state):
        res.append(path.copy())   # COPY. path keeps mutating.
        return

    if is_impossible(state):      # prune early, prune hard
        return

    for choice in choices(state):
        path.append(choice)       # 1. choose
        backtrack(advance(state)) # 2. explore
        path.pop()                # 3. un-choose  <- the whole pattern
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Return only the **count** of valid strings | Stop backtracking. This is the Catalan recurrence — do it with DP in O(n²), or the closed form C(2n,n)/(n+1). |
| Allow three bracket types `()[]{}` | The state is no longer two counters; you need an actual stack of which bracket is open, and the close guard becomes "the top of the stack matches". |
| **Remove Invalid Parentheses** (LC 301) | Same tree, but you also branch on *deleting* a character, and you BFS by deletion count so you find the minimum-removal answers first. |
| **Longest Valid Parentheses** (LC 32) | Not backtracking at all — the answer is a single number, so a stack scan or DP in O(n) wins. Recognising this switch is the real test. |

## How to think about it next time

Before writing any backtracking code, answer three questions out loud: **(1) What is one choice?** Here: append "(" or append ")". **(2) When am I done?** Here: openN == closeN == n. **(3) What makes a choice illegal, and can I check it before I make it?** Here: yes, from the two counters alone. If the answer to (3) is "I can only tell at the end", your solution will still be correct but slow, and that is exactly the gap between this problem and problem 39. Fill it in by asking what invariant every prefix of a valid answer must satisfy.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/generate-parentheses)
