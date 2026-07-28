# 773. Sliding Puzzle
> **Hard** &nbsp;&middot;&nbsp; BFS on a state graph &nbsp;&middot;&nbsp; family: **Graphs, BFS & DFS**

Rated Hard because of the modelling, not the algorithm. Once you see that a board *is* a node and a move *is* an edge, it is textbook BFS on a graph with 720 vertices.

**▶ [Step through this solution line by line](./visualization.html)** — 21 steps, traced on `board = [[1,2,3],[0,4,5]]`.

| | |
|---|---|
| time | O(6! × 6) — at most 720 states, up to 4 neighbours each |
| space | O(6!) for the visited set |

## The idea

**State-space BFS.** When a problem asks for the minimum number of operations to transform something, define a graph where *every configuration is a node* and *every legal operation is an edge*, then BFS. The art is choosing a state encoding that is cheap to hash — here, a 6-character string.

## How to recognise it

- "Minimum number of moves / steps / operations to reach a goal." Minimum + unweighted edges = BFS, always.
- The state space is finite and not too large. Count it before you start: 6! = 720 here, which is tiny.
- Contrast: DFS finds *a* solution, BFS finds the **shortest**. If edges had different costs, you would need Dijkstra instead (see LC 1631 in your repo).

## Where people go wrong

- **Marking visited on dequeue instead of enqueue.** The same state gets queued many times, and the queue explodes. Mark when you push.
- **Using DFS.** It will find a solution, just not the shortest one — and it may recurse very deep.
- **An unhashable state.** A list of lists cannot go in a set. Flatten to a string or a tuple.
- **Forgetting the already-solved case.** Line 10 returns 0 before any search.
- **Forgetting −1.** Half of all 2×3 board arrangements are unreachable from the goal — a parity invariant — so the queue really can drain.

## The reusable template

```python
# BFS on a state graph - the shape is always this
from collections import deque

q = deque([(start, 0)])
seen = {start}                      # hashable encoding: string or tuple
while q:
    state, dist = q.popleft()       # popLEFT = breadth-first
    if state == target:
        return dist
    for nxt in neighbours(state):
        if nxt not in seen:
            seen.add(nxt)           # mark on ENQUEUE, not on dequeue
            q.append((nxt, dist + 1))
return -1                            # target unreachable

# weighted edges instead? -> heapq and Dijkstra.
# huge state space? -> A* with an admissible heuristic.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Open the Lock** (LC 752) | Identical shape — states are 4-digit strings, edges turn one wheel. |
| **Word Ladder** (LC 127) | States are words, edges change one letter. |
| **Minimum Genetic Mutation** (LC 433) | Same again with gene strings. |
| Bigger board (8-puzzle, 15-puzzle) | 9! = 362,880 is still fine; 16! is not. Use A* with a Manhattan-distance heuristic. |
| Weighted moves | Dijkstra instead of BFS — a priority queue instead of a plain queue. |

## How to think about it next time

Train yourself to hear "minimum number of steps" as "**shortest path in an unweighted graph**", even when there is no graph in sight. Then answer three questions: what is a node (a full configuration), what is an edge (one legal operation), and how do I encode a node so it is hashable. Once those are answered the code is the same twelve lines every time — which is why Open the Lock, Word Ladder and this problem are genuinely the same problem.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/sliding-puzzle)
