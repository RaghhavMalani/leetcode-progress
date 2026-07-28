# 138. Copy List With Random Pointer
> **Medium** &nbsp;&middot;&nbsp; Hash map old→new · two-pass clone &nbsp;&middot;&nbsp; family: **Hashing**

The general recipe for deep-copying any linked structure: pass one creates the nodes, pass two wires them through an old→new map. And `map[null] = null` deletes every null check.

**▶ [Step through this solution line by line](./visualization.html)** — 19 steps, traced on `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`.

| | |
|---|---|
| time | O(n) — two passes |
| space | O(n) for the map; O(1) achievable by interleaving |

## The idea

Deep-copying a structure with **arbitrary internal references** is always two phases: **(1) create every node** so that a mapping old→new exists for all of them, then **(2) translate each pointer** by looking its target up in that map. One phase cannot work, because a pointer may target a node you have not reached yet.

## How to recognise it

- Clone / deep copy of a graph, list, or tree with cross-links.
- Any structure where `node.x` can point anywhere, not just forward.
- Exactly the same recipe solves LC 133 Clone Graph and LC 1485 Clone Binary Tree with Random Pointer.

## Where people go wrong

- **Wiring in pass one.** `copy->random` may refer to a node that does not exist yet.
- **Forgetting the null entry.** Without `oldcopy[nullptr] = nullptr` every dereference needs a guard, and `map[nullptr]` on a missing key would default-construct a null anyway in C++ — but relying on that accidentally is worse than stating it.
- **Shallow copying.** Returning the original head, or copying nodes but reusing the original pointers, passes trivial tests and fails the real ones.
- **Not knowing the O(1)-space version.** Interleave each clone directly after its original, set randoms via `orig->next->random = orig->random->next`, then unweave. It is the standard follow-up.

## The reusable template

```python
# deep copy ANY structure with arbitrary internal references
old_to_new = {None: None}          # identity entry -> no null checks later

cur = head                          # pass 1: CREATE every node, no pointers
while cur:
    old_to_new[cur] = Node(cur.val)
    cur = cur.next

cur = head                          # pass 2: TRANSLATE every pointer
while cur:
    c = old_to_new[cur]
    c.next   = old_to_new[cur.next]
    c.random = old_to_new[cur.random]
    cur = cur.next

return old_to_new[head]
# O(1) space variant: interleave clone after each original, wire randoms via
#   orig.next.random = orig.random.next, then unweave the two lists.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Clone Graph** (LC 133) | Same map, but built during a DFS or BFS since there is no linear order. |
| **Clone Binary Tree with Random Pointer** (LC 1485) | Identical recipe on a tree. |
| O(1) space | Interleave, wire, unweave — three passes, no map. |
| Deep copy with cycles | The map also serves as the visited set, so cycles are handled for free. |

## How to think about it next time

Memorise the recipe rather than the problem: **"map from old object to new object, create everything first, translate references second."** That sentence solves every deep-copy question you will ever be asked, in any language, for any structure. And notice the general trick of `map[null] = null` — inserting an identity entry for the degenerate case so the main loop needs no branches. That idea (like sentinel nodes and padded prefix arrays) turns special cases into ordinary ones.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer)
