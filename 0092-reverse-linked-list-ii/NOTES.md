# 92. Reverse Linked List II
> **Medium** &nbsp;·&nbsp; Linked list · partial reversal + seams &nbsp;·&nbsp; family: **Linked lists**

LC 206 applied to a slice. The reversal is the easy part; the two *seams* — anchor to new head, old head to remainder — are the whole difficulty, and the order of those two lines matters.

**▶ [Step through this solution line by line](../visualizations/0092-reverse-linked-list-ii.html)** — 14 steps, traced on `head = [1,2,3,4,5], left = 2, right = 4`.

| | |
|---|---|
| time | O(n) — one pass |
| space | O(1) |

## The idea

Reversing a middle section leaves two broken edges. Before you write a line, name the four nodes involved: the **anchor** (before the section), the **old head** (which becomes the tail), the **old tail** (which becomes the head), and the **remainder**. Then the reconnection is two assignments and you cannot get lost.

## How to recognise it

- Reverse / rotate / modify a **sub-range** of a linked list.
- Any "reverse in groups of k" question (LC 25) is this, repeated.
- The presence of 1-based indices `left` and `right` in a list problem is a strong hint you will need a dummy for the `left == 1` case.

## Where people go wrong

- **Reconnecting in the wrong order.** `lp.next = prev` before `lp.next.next = l` destroys the reference to the old head. Line 25 must come first.
- **No dummy when `left == 1`.** There is no anchor node, so you need a separate branch. The dummy provides one for free.
- **Off-by-one in the loop counts.** `left - 1` steps to reach the anchor; `right - left + 1` iterations to reverse. Both are inclusive-range arithmetic and both are easy to get wrong — check on paper with left = right.
- **Trying to do it without a trailing pointer.** You need the anchor; there is no way back.

## The reusable template

```python
# Reverse the slice [left, right] - name your four nodes first
dummy = ListNode(0, head)
lp = dummy
for _ in range(left - 1):        # lp = the ANCHOR, just before the slice
    lp = lp.next

prev, cur = None, lp.next        # cur = OLD HEAD (becomes the tail)
for _ in range(right - left + 1):
    cur.next, prev, cur = prev, cur, cur.next
# now: prev = OLD TAIL (new head),  cur = REMAINDER

lp.next.next = cur               # seam 1: old head -> remainder   (FIRST)
lp.next      = prev              # seam 2: anchor  -> new head
return dummy.next
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Reverse the whole list | LC 206 — left = 1, right = n, no seams needed. |
| **Reverse Nodes in k-Group** (LC 25) | This, in a loop, with the anchor moving forward each time. Genuinely hard, and this problem is the prerequisite. |
| **Rotate List** (LC 61) | Find the new tail, cut, and reattach — different mechanics, same "name your four nodes" discipline. |
| Swap nodes in pairs | LC 24 — k-group with k = 2. |

## How to think about it next time

The transferable habit: **before mutating a linked structure, write down every pointer that will be broken and where each broken end must end up.** Four names on paper turn this from a puzzle into bookkeeping. It is the same discipline that makes tree rotations and doubly-linked-list splices routine, and it is the reason experienced people write these correctly on the first attempt while everyone else debugs for twenty minutes.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/reverse-linked-list-ii)
