# 1260. Shift 2D Grid
> **Easy** &nbsp;&middot;&nbsp; Flatten · modular shift · unflatten &nbsp;&middot;&nbsp; family: **Math & number theory**

Two ideas that pay off far beyond this problem: `k %= total` to collapse a huge shift, and flatten-shift-unflatten to delete every wrap-around special case.

**▶ [Step through this solution line by line](./visualization.html)** — 12 steps, traced on `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1`.

| | |
|---|---|
| time | O(m·n) |
| space | O(m·n) for the output |

## The idea

A 2D grid in row-major order **is** a 1D array. Once you accept that, "shift with wrap-around" is a single modular addition, and the three awkward cases (stay in row, move to next row, wrap to the top) disappear. The conversions are `flat = r·cols + c` and back `r = flat // cols`, `c = flat % cols`.

## How to recognise it

- Any grid operation that is naturally linear: shifting, spiralling, snake traversal, diagonal indexing.
- A shift/rotation amount much larger than the container — always reduce modulo the size first.
- The same flattening makes a sorted 2D matrix binary-searchable as one array (LC 74).

## Where people go wrong

- **Skipping `k %= total`.** With k = 10⁹ and a naive per-step shift you time out; even here it avoids meaningless work.
- **Shifting in place.** You overwrite cells you have not read yet. Write into a fresh grid, or work backwards.
- **Confusing rows and columns in the conversion.** It is `r * COLS + c`, never `r * ROWS + c`. On a square grid the bug is invisible; on a rectangular one it corrupts everything.
- **Shifting one step k times.** O(k·m·n) instead of O(m·n).

## The reusable template

```python
# flatten -> shift -> unflatten. no wrap-around case analysis at all.
total = m * n
k %= total                       # ALWAYS reduce first: k can be 1e9

result = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        flat = i * n + j                 # r * COLS + c  (never * ROWS)
        dest = (flat + k) % total
        result[dest // n][dest % n] = grid[i][j]
return result
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Rotate Array** (LC 189) | 1D version — three reversals, O(1) space. |
| **Search a 2D Matrix** (LC 74) | Binary search over the flattened index. |
| **Rotate Image** (LC 48) | Transpose then reverse rows — a different transform, still index arithmetic. |
| Spiral order (LC 54) | Boundary shrinking; flattening does not help here. |

## How to think about it next time

Add one question to your grid checklist: **"can I treat this as a 1D array?"** If the operation respects row-major order, flattening removes an entire dimension of edge cases. And more generally — whenever an operation repeats with a period, reduce the count modulo that period *first*. Rotations, shifts, cyclic permutations, and repeated string operations all collapse this way, and forgetting to do it is the most common cause of timeouts on otherwise-correct code.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/shift-2d-grid)
