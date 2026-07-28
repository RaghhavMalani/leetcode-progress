# 2. Add Two Numbers
> **Medium** &nbsp;&middot;&nbsp; Linked list · digit-by-digit carry &nbsp;&middot;&nbsp; family: **Linked lists**

Long addition on a list. The whole problem is the loop condition: `while l1 or l2 or carry` — three reasons to keep going, and forgetting the third is the classic failure.

**▶ [Step through this solution line by line](./visualization.html)** — 26 steps, traced on `l1 = [2,4,3], l2 = [5,6,4]   (342 + 465)`.

| | |
|---|---|
| time | O(max(m, n)) |
| space | O(max(m, n)) for the output |

## The idea

Simulate the algorithm you learned at seven. Two things make it clean: **treat a missing digit as 0** so you need no separate "one list is longer" loop, and **include the carry in the loop condition** so a final overflow digit gets emitted without a special case after the loop.

## How to recognise it

- Digits in a list or array, arithmetic that carries — addition, multiplication, incrementing.
- Least-significant-first storage means no reversing. Most-significant-first (LC 445) means you must reverse or use a stack — check which you have been given, first thing.
- Big-integer arithmetic in general: the carry loop is the same whether the base is 10, 2, or 2³².

## Where people go wrong

- **Dropping `carry` from the loop condition.** 5 + 5 returns [0] instead of [0,1]. This is the bug the problem is built to catch.
- **Writing separate loops for "both lists", "l1 only", "l2 only".** Correct but three times the code and three times the chance of a bug. The `if l1 else 0` collapses them.
- **Converting to int, adding, converting back.** Works in Python, fails in every other language, and dodges the exercise. Say why you are not doing it.
- **Advancing the input pointers before reading them.** Read, compute, then advance.

## The reusable template

```python
# Digit-by-digit with carry - the loop condition does the work
dummy = ListNode(); cur = dummy; carry = 0
while l1 or l2 or carry:                  # THREE reasons to continue
    v1 = l1.val if l1 else 0              # missing digit = 0
    v2 = l2.val if l2 else 0
    carry, digit = divmod(v1 + v2 + carry, 10)
    cur.next = ListNode(digit); cur = cur.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
return dummy.next
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Most-significant digit first | LC 445 — reverse both lists, or push onto two stacks and pop. |
| **Plus One** (LC 66) | An array, and only a +1 carry. Same loop, walked backwards. |
| **Multiply Strings** (LC 43) | Grade-school multiplication into an m+n buffer, then one carry pass. |
| Add binary strings | LC 67 — identical, with base 2 instead of 10. |

## How to think about it next time

Notice how much complexity the loop condition absorbed. When you write a simulation, **spend your effort on the loop condition and the "missing value" defaults**, not on adding branches after the loop. A good test: if your code has a chunk of clean-up logic after the main loop, ask whether the loop condition could have covered it. Usually it can, and the result is shorter and easier to argue is correct.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/add-two-numbers)
