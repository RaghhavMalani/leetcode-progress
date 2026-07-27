# 1929. Concatenation of Array
> **Easy** &nbsp;·&nbsp; Index arithmetic · pre-sized output &nbsp;·&nbsp; family: **Math & number theory**

Trivial, but it demonstrates a habit worth having: pre-size the output and write with an index offset rather than appending twice.

**▶ [Step through this solution line by line](../visualizations/1929-concatenation-of-array.html)** — 6 steps, traced on `nums = [1,3,2,1]`.

| | |
|---|---|
| time | O(n) |
| space | O(n) for the output |

## The idea

**Pre-size, then index.** When you know the output length in advance, allocate once and write by index. Appending repeatedly is amortised O(1) in most languages but involves reallocation and copying, and in C++ `reserve`/sizing is measurably faster.

## How to recognise it

- The output size is a known function of the input size.
- You want to fill several positions per iteration — an offset makes that one loop instead of two.
- The same index arithmetic — `i + n`, `i % n`, `i * cols + j` — is the backbone of circular buffers and flattened matrices.

## Where people go wrong

- **Two separate loops (or `nums + nums`).** Perfectly correct and shorter in Python. The single loop is a C++ habit worth understanding rather than a requirement.
- **Appending to an already-sized vector.** `vector<int> result(2*n)` then `push_back` gives you 3n elements — the classic C++ slip.
- **Off-by-one in the offset.** The second copy starts at index n, not n−1 or n+1.

## The reusable template

```python
# pre-size the output, then write by index offset
result = [0] * (2 * n)
for i in range(n):
    result[i]     = nums[i]
    result[i + n] = nums[i]      # one loop fills BOTH copies

# the three index conversions worth owning:
#   flatten   idx = r * cols + c
#   unflatten r = idx // cols,  c = idx % cols
#   wrap      idx = (idx + k) % total
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Shift 2D Grid** (LC 1260) | Flatten with `i*n + j`, shift with `% total`, unflatten with `/n` and `%n`. Also in your repo. |
| Rotate an array by k | Reverse three times, or write to `(i + k) % n`. |
| Circular buffer | `(head + size) % capacity`. See LC 622 in your repo. |
| Concatenate k copies | Same loop with `i + c*n` for each copy c. |

## How to think about it next time

Easy problems are where index arithmetic becomes automatic. Get comfortable with the three conversions — **flatten** (`r*cols + c`), **unflatten** (`idx/cols`, `idx%cols`), and **wrap** (`% n`) — because they show up in grid problems, circular queues, matrix rotation and hashing, and fumbling them in a hard problem costs you far more than the two minutes it takes to drill them here.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/concatenation-of-array)
