# 1840. Maximum Building Height
> **Hard** &nbsp;&middot;&nbsp; Constraint propagation · two sweeps + geometry &nbsp;&middot;&nbsp; family: **Prefix sums & intervals**

Three ideas stacked: sentinel restrictions to kill edge cases, two sweeps to propagate a neighbour constraint in both directions, and a closed-form tent peak between each adjacent pair.

**▶ [Step through this solution line by line](./visualization.html)** — 15 steps, traced on `n = 5, restrictions = [[2,1],[4,1]]`.

| | |
|---|---|
| time | O(m log m) where m is the number of restrictions |
| space | O(m) |

## The idea

A constraint that relates **neighbours** must be propagated in **both directions** before any value is final — hence the left-to-right sweep followed by the right-to-left sweep. Then, between two fixed points, the tallest reachable value follows from a slope-1 "tent": rise from both sides and meet in the middle, giving `(hL + hR + distance) // 2`.

## How to recognise it

- Constraints of the form |f(i) − f(j)| ≤ |i − j| — heights, timestamps, positions with a speed limit.
- A follow-the-neighbour rule plus fixed anchor points. Two sweeps is the standard tool; it also solves LC 135 Candy.
- Very large n (10⁹) with few restrictions — you must reason about the gaps analytically, not iterate over buildings.

## Where people go wrong

- **Only sweeping one direction.** A restriction to the right of a building constrains it just as much as one to the left.
- **Forgetting the sentinels.** Without [1, 0] the first building is unconstrained; without [n, n−1] the last gap is computed wrongly. They also remove all the boundary branches.
- **The tent formula.** `(hL + hR + dist) // 2` — derive it once: the peak p satisfies p − hL ≤ x and p − hR ≤ dist − x, and the best x makes both tight. Integer division handles the parity case.
- **Iterating over all n buildings.** n can be 10⁹; only the restriction points and the gaps between them matter.

## The reusable template

```python
# 1. sentinels turn boundary RULES into ordinary data
restrictions += [[1, 0], [n, n - 1]]
restrictions.sort()

# 2. propagate the neighbour constraint BOTH ways
for i in range(1, m):                       # left -> right
    d = restrictions[i][0] - restrictions[i-1][0]
    restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + d)

for i in range(m - 2, -1, -1):              # right -> left
    d = restrictions[i+1][0] - restrictions[i][0]
    restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + d)

# 3. peak of the "tent" between each adjacent pair
ans = max((hL + hR + (idR - idL)) // 2 for consecutive pairs)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Candy** (LC 135) | The same two-sweep constraint propagation, taking a max instead of a min. |
| Slope other than 1 | Multiply the distance term by the slope throughout. |
| Minimum height instead of maximum | Sweep with max instead of min, and the tent becomes a valley. |
| Restrictions may be infeasible | Detect it when a sweep would force a negative height. |

## How to think about it next time

Two habits worth extracting. First: **when a rule links neighbours, one pass is never enough** — information flows both ways, so sweep forwards then backwards. That single pattern solves Candy, this problem, and several "smooth the array" questions. Second: **add sentinel entries to encode boundary rules as data** rather than as branches. Both are ways of turning special cases into ordinary cases, which is most of what makes hard problems writable.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/maximum-building-height)
