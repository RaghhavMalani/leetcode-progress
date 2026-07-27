# 2196. Create Binary Tree From Descriptions
> **Medium** &nbsp;·&nbsp; Hash map · build a structure from edges &nbsp;·&nbsp; family: **Hashing**

Building a tree from an unordered edge list. Two ideas: a value→node map so nodes are created once and shared, and finding the root by elimination — the only value that is never a child.

**▶ [Step through this solution line by line](../visualizations/2196-create-binary-tree-from-descriptions.html)** — 25 steps, traced on `descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`.

| | |
|---|---|
| time | O(n) |
| space | O(n) |

## The idea

Two reusable ideas. **Create-on-demand via a map:** when edges arrive in arbitrary order, a `value → object` dictionary lets you reference a node before you have seen it "declared". **Find the root by elimination:** in a tree, exactly one node has no parent, so root = all_nodes − all_children.

## How to recognise it

- A structure specified by an unordered list of edges or parent/child pairs.
- Any time you must "find the root/start/source" of a DAG or tree — it is the node with in-degree 0. The same idea starts topological sort (see LC 3620 in your repo).
- Adjacency lists in general are built exactly this way.

## Where people go wrong

- **Creating a new node per description.** Then node 20 exists twice and the tree fragments. The `if value not in nodes` guard is essential.
- **Assuming descriptions come parent-first.** They do not, which is precisely why creation must be on demand.
- **Looking for the root before the loop finishes.** A node can look parentless until a later description names it as a child.
- **Using a set of nodes instead of a dict.** You need the actual object to attach children to, not just the value.

## The reusable template

```python
# create-on-demand + find the root by elimination
nodes, children = {}, set()
for parent, child, is_left in descriptions:
    if parent not in nodes: nodes[parent] = TreeNode(parent)   # ONCE each
    if child  not in nodes: nodes[child]  = TreeNode(child)
    if is_left: nodes[parent].left  = nodes[child]
    else:       nodes[parent].right = nodes[child]
    children.add(child)

for value in nodes:                 # exactly one node has no parent
    if value not in children:
        return nodes[value]

# same idea: DAG sources = in-degree 0 -> the start of a topological sort
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Build an adjacency list from an edge list | The same create-on-demand pattern with lists. |
| **Clone Graph** (LC 133) | A map from original node → copy, filled as you traverse. |
| **Copy List with Random Pointer** (LC 138) | Same old→new map. Also in your repo. |
| Detect a cycle / not-a-tree | Check that exactly one node has in-degree 0 and that the edge count is n−1. |
| **Topological sort** | Start from all in-degree-0 nodes. LC 3620 in your repo uses it. |

## How to think about it next time

Whenever a structure is described by edges rather than by nesting, reach for **a dictionary keyed by identity** and create objects lazily. And remember the general "find the entry point" move: **the root is what nothing points to**. In-degree zero identifies tree roots, DAG sources, and topological-sort starting points — all the same observation, and it turns "where do I begin?" into a set difference.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions)
