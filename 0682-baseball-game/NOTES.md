# 682. Baseball Game
> **Easy** &nbsp;&middot;&nbsp; Stack · simulation with undo &nbsp;&middot;&nbsp; family: **Stacks & monotonic stacks**

A stack chosen for one specific reason: the "C" operation needs an *undo*, and a running total cannot undo. Recognising which operation forces the data structure is the whole lesson.

**▶ [Step through this solution line by line](./visualization.html)** — 15 steps, traced on `operations = ["5","2","C","D","+"]`.

| | |
|---|---|
| time | O(n) |
| space | O(n) |

## The idea

The data structure is chosen by the **hardest single operation**, not the most common one. Three of these four operations would work fine with a running total. "C" — remove the most recent thing — is what forces a stack, and that one requirement decides the design.

## How to recognise it

- Operations that reference "the last", "the previous two", or that **undo**.
- Nesting or matching — brackets, tags, function calls — is the other classic stack signal.
- Expression evaluation, especially postfix / RPN.

## Where people go wrong

- **Not handling negative numbers.** `op.isdigit()` returns False for "-5". Using `else: int(op)` as the fallback, as this solution does, is the robust ordering.
- **Indexing `stack[-2]` without checking length.** The problem guarantees validity; an interviewer might not.
- **Maintaining a running sum alongside the stack.** A fine optimisation, but now "C" has to subtract too and you have two things to keep in sync. Summing once at the end is simpler and just as fast.

## The reusable template

```python
# Stack simulation - the structure is chosen by the hardest operation
stack = []
for op in operations:
    if   op == '+': stack.append(stack[-2] + stack[-1])
    elif op == 'D': stack.append(stack[-1] * 2)
    elif op == 'C': stack.pop()              # <- THIS is why it is a stack
    else:           stack.append(int(op))    # else, not isdigit(): handles "-5"
return sum(stack)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Valid Parentheses** (LC 20) | Push openers, pop and match closers. |
| **Evaluate RPN** (LC 150) | Pop two, apply, push. Same skeleton. |
| **Min Stack** (LC 155) | A second stack of running minima so `getMin` is O(1). |
| **Basic Calculator** (LC 224 / 227) | Stacks for numbers and operators, plus precedence. The serious version. |
| **Simplify Path** (LC 71) | ".." is exactly a "C" operation on directory names. |

## How to think about it next time

Make this your habit when choosing a data structure: **list every operation the problem requires, and pick for the most demanding one.** Need the most recent thing → stack. The oldest → queue. The largest → heap. Membership → set. Order-and-rank → sorted structure or BIT. Most "which structure?" questions are decided by a single operation, and finding that operation takes ten seconds and saves a rewrite.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/baseball-game)
