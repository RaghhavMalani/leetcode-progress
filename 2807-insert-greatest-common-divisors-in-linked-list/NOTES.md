# 2807. Insert Greatest Common Divisors in Linked List
> **Medium** &nbsp;·&nbsp; Linked list · insert between pairs &nbsp;·&nbsp; family: **Linked lists**

The only real trap is the advance step: after inserting, you must move forward **two** nodes, not one — otherwise you keep inserting between your own insertions.

**▶ [Step through this solution line by line](../visualizations/2807-insert-greatest-common-divisors-in-linked-list.html)** — 14 steps, traced on `head = [18,6,10,3]`.

| | |
|---|---|
| time | O(n log maxValue) — one gcd per adjacent pair |
| space | O(1) extra |

## The idea

When you **modify a structure while traversing it**, the advance step has to account for what you just added. Insert one node between curr and curr->next, and the correct next position is `curr->next->next`. Getting this wrong produces either an infinite loop or a silently wrong list.

## How to recognise it

- Any "insert between every adjacent pair" or "duplicate every element" operation on a list or array.
- The head never changes here, so no dummy node is needed — worth noticing, since most list problems do need one.
- The same care applies when deleting during traversal: you must capture the successor before unlinking.

## Where people go wrong

- **`curr = curr->next` after inserting.** You land on the gcd node you just made and start inserting between it and the original — infinite loop, or at best a corrupted list.
- **Not capturing `curr->next` before rewiring.** The constructor here does it in one expression, which is why no temporary appears.
- **Assuming a dummy is always needed.** It is not — only when the head can change.
- **Recursive gcd.** Fine, but the iterative version is shorter and has no depth concern.

## The reusable template

```python
# insert between every adjacent pair - then advance TWO
curr = head
while curr.next:
    g = gcd(curr.val, curr.next.val)
    curr.next = ListNode(g, curr.next)    # splice in one expression
    curr = curr.next.next                 # HOP OVER the node just inserted
return head                                # head never changes -> no dummy

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Insert the SUM / difference between pairs | Identical loop, different expression. |
| **Odd Even Linked List** (LC 328) | Rearrange rather than insert — two chains, then splice. |
| Delete every second node | The mirror operation; capture the successor first. |
| **Find GCD of Array** (LC 1979) | Euclid on a whole array. Also in your repo. |

## How to think about it next time

Whenever you mutate a container while iterating it, **write down where the cursor should be after the mutation** before you write the loop. For "insert one, skip it" the answer is two hops; for "delete one" it is zero hops (the cursor already points past it). Making that explicit prevents both of the classic failures — infinite loops and skipped elements — and it is exactly the discipline that makes linked-list code correct on the first try.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list)
