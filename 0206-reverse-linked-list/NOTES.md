# 206. Reverse Linked List
> **Easy** &nbsp;·&nbsp; Linked list · pointer rewiring &nbsp;·&nbsp; family: **Linked lists**

The single most reused linked-list primitive. Four lines in a fixed order — save, flip, advance, advance — and getting the order wrong loses the rest of the list forever.

**▶ [Step through this solution line by line](../visualizations/0206-reverse-linked-list.html)** — 17 steps, traced on `head = [1,2,3]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) — the recursive version is O(n) stack, which matters |

## The idea

Linked list problems are almost never about algorithms; they are about **not losing your grip on a node**. You have no random access, so the moment you overwrite a `next` pointer, everything downstream is unreachable unless you saved it. Every list problem is this discipline plus a little bookkeeping.

## How to recognise it

- Any problem that needs the list in the opposite direction, or needs to compare a list with its reverse (palindrome).
- It appears as a **subroutine** far more often than as a problem: LC 143 reorder, LC 92 reverse-a-sublist, LC 25 reverse-in-k-groups, LC 234 palindrome list.
- Whenever you catch yourself wanting `node.prev` in a singly linked list, reversal is usually the answer.

## Where people go wrong

- **Flipping before saving.** `curr.next = prev` then `curr = curr.next` walks you backwards into the part you already reversed — an infinite loop.
- **Returning `curr` instead of `prev`.** When the loop ends `curr` is None. The new head is always `prev`.
- **Forgetting that the old head becomes the tail** and must end up pointing at None. It does automatically here, because `prev` starts as None — that initial value is doing real work.
- **The recursive version.** Elegant, but O(n) stack and it will overflow on a 5000-node list. Say that when you offer it.

## The reusable template

```python
# Reverse a singly linked list - the four-line dance
prev, curr = None, head
while curr:
    nxt = curr.next        # 1. SAVE the rest of the list
    curr.next = prev       # 2. flip this node's arrow backwards
    prev = curr            # 3. prev catches up
    curr = nxt             # 4. curr moves on
return prev                # prev is the new head; curr is None
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Reverse only nodes m..n | LC 92 — same loop, run it exactly n−m+1 times, then reattach both seams. Your repo has this. |
| Reverse in groups of k | LC 25 — the same loop k times, repeatedly. The hardest of the family. |
| **Palindrome linked list** (LC 234) | Find the middle with fast/slow, reverse the second half, compare. |
| **Reorder list** (LC 143) | Split, reverse the second half, interleave. Also in your repo. |
| Doubly linked list | Swap `prev` and `next` on every node; no saving needed since you can always go back. |

## How to think about it next time

Drill this until it is muscle memory, because it shows up as a *step* inside harder problems. The general habit for list problems: **draw three or four nodes and physically point at them as you execute each line.** Nearly every bug in this category is visible in ten seconds on paper and invisible for twenty minutes in your head. Also learn the two universal helpers — a **dummy head** (removes all the "what if it is the first node" special cases) and **fast/slow pointers** (finds the middle, detects cycles, finds the nth from the end).

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/reverse-linked-list)
