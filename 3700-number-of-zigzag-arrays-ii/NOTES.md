# 3700. Number of Zigzag Arrays II
> **Hard** &nbsp;&middot;&nbsp; Matrix exponentiation of a linear recurrence &nbsp;&middot;&nbsp; family: **Dynamic programming**

Part I with n up to 10¹⁸. The DP transition is linear, so encode it as a matrix and apply it n times with binary exponentiation — O(log n) instead of O(n).

**▶ [Step through this solution line by line](./visualization.html)** — 11 steps, traced on `n = 4, value range of size m = 2`.

| | |
|---|---|
| time | O(m³ log n) |
| space | O(m²) |

## The idea

Any DP whose transition is a **fixed linear map** — new state = matrix × old state, with the matrix not depending on the step — can be advanced n steps by computing T^n. And T^n takes only O(log n) matrix multiplications via binary exponentiation: square repeatedly, multiply in wherever the exponent has a set bit.

## How to recognise it

- **n up to 10¹⁸** (or any bound far beyond what a loop can reach) with a per-step recurrence. That constraint alone is the signal.
- The state has fixed, small dimension and each new component is a linear combination of old ones — no products of two state variables, no conditionals on the step.
- The classic instance is Fibonacci in O(log n); everything else is the same idea with a bigger matrix.

## Where people go wrong

- **A non-linear transition.** If the recurrence multiplies two state variables, or depends on the step index, matrix exponentiation does not apply.
- **Exponent off by one.** Here it is n − 2, because the base case already represents length-2 arrays. Verify on the smallest n by hand.
- **Cost of the matrix multiply.** O(m³) per multiply, so this is only worthwhile when m is small. If m is large but the matrix is structured (banded, circulant), exploit that instead.
- **Modulus placement.** Reduce inside the innermost accumulation, or the intermediate sums overflow.
- **Multiplying matrix × matrix when vector × matrix would do.** Applying T to a vector is O(m²); only the squaring needs O(m³).

## The reusable template

```python
# linear transition + huge n  ->  matrix exponentiation, O(dim^3 log n)
def mat_mul(A, B): ...          # O(dim^3)
def mat_vec(A, v): ...          # O(dim^2) - cheaper, use it for the state

state = base_case_vector        # flatten ALL dp arrays into ONE vector
T     = transition_matrix       # T[i][j] = coefficient of old j in new i

power = n - 2                   # check this offset on the smallest n by hand
while power:
    if power & 1:
        state = mat_vec(T, state)
    T = mat_mul(T, T)           # square: T now covers twice as many steps
    power >>= 1

return sum(state) % MOD
# requires: the transition is the SAME every step and LINEAR in the state.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part I** (LC 3699) | n is small, so the plain O(n·m) prefix-sum DP is enough. Also in your repo. |
| Fibonacci for huge n | The 2×2 matrix [[1,1],[1,0]] raised to the nth power. |
| Counting walks of length n in a graph | A^n[i][j] is exactly the number of walks — the same operation. |
| Linear recurrence with a constant term | Add one row and column to absorb the constant into the matrix. |
| Very large m | Matrix exponentiation dies; look for a closed form or a polynomial-based method (Kitamasa). |

## How to think about it next time

Build the habit of checking two things whenever you see an enormous n: **is the transition the same at every step, and is it linear?** If both are yes, you can jump n steps in O(log n) and the size of n stops mattering. This is one of a small family of "escape hatches" for huge inputs — the others being closed forms, binary exponentiation on numbers, and periodicity arguments (find the cycle, then take n mod period). Recognising which escape hatch applies is usually the entire problem.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii)
