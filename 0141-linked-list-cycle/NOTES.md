# 141. Linked List Cycle
> **Easy** &nbsp;·&nbsp; Fast & slow pointers · Floyd &nbsp;·&nbsp; family: **Two pointers & sliding window**

The tortoise and the hare. Why it must work: inside a loop the gap between fast and slow shrinks by exactly one every iteration, so it reaches zero — they cannot step over each other.

**▶ [Step through this solution line by line](../visualizations/0141-linked-list-cycle.html)** — 14 steps, traced on `head = [3,2,0,-4], tail connects to index 1`.

| | |
|---|---|
| time | O(n) |
| space | O(1) — the whole point |

## The idea

Two pointers at different **speeds**. On a finite path the fast one runs out. On a cycle it laps the slow one. The proof is one sentence: once both are inside the loop, fast gains exactly one position per iteration, so the gap decreases by one each time and must hit zero — it can never jump over.

## How to recognise it

- "Does this list have a cycle", "does this sequence repeat", "will this process terminate".
- Explicit O(1) space. With space allowed, a visited set is trivially correct and much easier to explain.
- Applies to any **deterministic successor function**, not just lists — see LC 287 in your repo, and LC 202 Happy Number.

## Where people go wrong

- **Checking only `fast`, not `fast.next`.** `fast.next.next` then throws on an even-length acyclic list. Both checks are mandatory.
- **Comparing values instead of nodes.** `slow.val == fast.val` gives false positives on duplicate values. Compare identity.
- **Starting `fast` at `head.next`.** A workable variant, but then the initial `slow == fast` test must be handled differently. Pick one convention.
- **Believing the meeting point is the cycle start.** It is not — that needs the second phase (LC 142, and LC 287 in your repo).

## The reusable template

```python
# Fast & slow - three jobs, one shape

# 1. detect a cycle
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
        return True
return False

# 2. find the middle: run the same loop, then `slow` is the middle
# 3. find the cycle entrance: after they meet, reset one to head and
#    advance BOTH one step at a time (LC 142 / LC 287)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Find the cycle **entrance** | LC 142 — reset one pointer to the head, advance both one step at a time. |
| **Find the Duplicate Number** (LC 287) | The same algorithm on an array read as a functional graph. Also in your repo. |
| Cycle **length** | After meeting, keep one still and walk the other until it returns. |
| **Happy Number** (LC 202) | Digit-square-sum as the successor function — cycle detection on integers. |
| Middle of the list | Same pointers, but you stop when fast runs off rather than when they meet. |

## How to think about it next time

Fast/slow is a **whole toolkit, not one trick**. Learn the three jobs it does: detect a cycle (do they meet?), find the middle (where is slow when fast ends?), and locate a cycle entrance (phase two). Then learn the generalisation — it works on *any* function you can iterate, which is why array problems like LC 287 and number problems like LC 202 fall to it. When a problem says "O(1) space" and involves following pointers or repeatedly applying a function, this should be your first thought.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/linked-list-cycle)
