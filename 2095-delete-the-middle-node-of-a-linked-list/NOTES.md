# 2095. Delete the Middle Node of a Linked List
> **Medium** &nbsp;·&nbsp; Fast & slow pointers · find the middle &nbsp;·&nbsp; family: **Two pointers & sliding window**

Fast/slow doing its second job: finding the midpoint. The extra wrinkle is `prev` — to delete a node you need its predecessor, and a singly linked list will not give you one.

**▶ [Step through this solution line by line](../visualizations/2095-delete-the-middle-node-of-a-linked-list.html)** — 8 steps, traced on `head = [1,3,4,7,1,2,6]`.

| | |
|---|---|
| time | O(n) — one pass |
| space | O(1) |

## The idea

Same two pointers as cycle detection, different question. When fast has covered 2k steps, slow has covered k — so when fast hits the end, slow is at the middle. The only real decision is **which** middle: `while fast and fast.next` lands slow on the upper middle (index ⌊n/2⌋), which is what this problem defines.

## How to recognise it

- "Middle node", "split in half", "second half of the list" — including as a step inside LC 143 and LC 234.
- Deleting in a singly linked list always means "find the predecessor", so you need either a trailing pointer or a dummy.
- If you can afford two passes, counting the length and walking n//2 is simpler and completely acceptable — say so first.

## Where people go wrong

- **Which middle.** `while fast and fast.next` vs `while fast.next and fast.next.next` give the upper and lower middle. On an even-length list they differ, and the problem statement decides which is right. Check with n = 4 on paper.
- **Forgetting `prev`.** You end up at the node you want to delete with no way to unlink it.
- **Not guarding the single-node case.** `prev` stays None and `prev.next` throws. Line 8 exists for exactly this.
- **A dummy would remove `prev` entirely** — start `slow = dummy` and the trailing pointer is free. Worth mentioning as a cleanup.

## The reusable template

```python
# Find the middle with fast & slow
slow = fast = head
while fast and fast.next:      # -> slow ends on the UPPER middle
    slow = slow.next
    fast = fast.next.next

# lower middle instead? use:  while fast.next and fast.next.next
# need the predecessor too?  start slow at a dummy in front of head
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Middle of the Linked List** (LC 876) | Return slow instead of deleting. |
| **Reorder List** (LC 143) | Find the middle, reverse the second half, interleave. Also in your repo. |
| **Palindrome Linked List** (LC 234) | Middle, reverse, compare. |
| **Sort List** (LC 148) | Middle to split, recurse, merge — merge sort on a list. |

## How to think about it next time

"Find the middle" is a **primitive**, not a problem. Four different Mediums in your repo and beyond are "find the middle" composed with one other primitive (reverse, merge, compare). Build the habit of asking after each solve: *what one-line capability did I just implement, and what does it compose with?* That is how a hundred solved problems becomes twenty remembered techniques instead of a hundred forgotten solutions.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list)
