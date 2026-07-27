# 21. Merge Two Sorted Lists
> **Easy** &nbsp;·&nbsp; Linked list · dummy head + merge &nbsp;·&nbsp; family: **Linked lists**

Two ideas worth stealing: the **dummy head** that deletes every empty-list special case, and the final one-line attach of the leftover tail.

**▶ [Step through this solution line by line](../visualizations/0021-merge-two-sorted-lists.html)** — 24 steps, traced on `list1 = [1,2,4], list2 = [1,3,4]`.

| | |
|---|---|
| time | O(m + n) |
| space | O(1) — nodes are relinked, not copied |

## The idea

The **dummy (sentinel) head** is the single highest-value trick in linked lists. Without it, every "append" has to ask "is the result empty?" and every "delete" has to ask "is this the head?". With it, every node has a predecessor and all those branches vanish.

## How to recognise it

- Two (or k) sorted sequences to combine while preserving order.
- Any list operation that might modify the head — delete, insert at front, merge. Reach for a dummy reflexively.
- This is also merge sort’s merge step, which is why LC 148 and LC 23 both call it.

## Where people go wrong

- **Returning `result` instead of `result.next`.** You return the dummy and every answer starts with a spurious 0.
- **Looping to attach the remainder.** Correct but pointless — one pointer assignment attaches an arbitrarily long tail.
- **Losing stability.** Using `>` vs `>=` decides which list wins a tie. It does not matter for values, but it does the moment nodes carry payloads, and interviewers ask.
- **Allocating new nodes.** Works, but throws away the O(1) space that makes the linked-list version interesting.

## The reusable template

```python
# Dummy head + merge - the shape behind LC 21, 23, 88, 148
dummy = ListNode()
tail  = dummy
while a and b:
    if a.val <= b.val:
        tail.next, a = a, a.next
    else:
        tail.next, b = b, b.next
    tail = tail.next

tail.next = a or b          # attach the WHOLE remainder in one line
return dummy.next           # skip the dummy
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Merge k sorted lists** (LC 23) | Pair them up and merge repeatedly — O(N log k). Your repo has this one; it calls this function. |
| Merge two sorted **arrays** in place | LC 88 — fill from the BACK so you never overwrite unread data. |
| **Sort a linked list** (LC 148) | Merge sort: split with fast/slow, recurse, merge with exactly this function. |
| Recursive merge | Four lines and very pretty, but O(m+n) stack depth. |

## How to think about it next time

Adopt this rule: **if a linked-list operation could touch the head, start with a dummy node.** It costs one line and removes an entire class of null-pointer bugs. The second habit from this problem: when you finish a loop, ask "what is left over, and can I attach it in O(1) instead of looping?" With linked lists the answer is usually yes, and that is precisely the advantage they have over arrays.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists)
