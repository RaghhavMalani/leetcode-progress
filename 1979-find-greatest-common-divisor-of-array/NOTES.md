# 1979. Find Greatest Common Divisor of Array
> **Easy** &nbsp;&middot;&nbsp; Number theory · Euclidean algorithm &nbsp;&middot;&nbsp; family: **Math & number theory**

One line if you know your library. Worth the visit for the Euclidean algorithm itself, which is the engine behind gcd, lcm, modular inverses and Diophantine equations.

**▶ [Step through this solution line by line](./visualization.html)** — 7 steps, traced on `nums = [2,5,6,9,10]`.

| | |
|---|---|
| time | O(n) to scan + O(log min) for the gcd |
| space | O(1) |

## The idea

**Euclid:** gcd(a, b) = gcd(b, a mod b), with gcd(a, 0) = a. It terminates in O(log min(a,b)) steps because the remainder at least halves every two iterations. This is the oldest non-trivial algorithm still in daily use, and it is worth being able to write from memory.

## How to recognise it

- Divisibility, common factors, reducing fractions, tiling a length with equal pieces.
- **lcm(a, b) = a // gcd(a, b) * b** — divide first to avoid overflow.
- The extended version solves `ax + by = gcd(a,b)`, which gives modular inverses — needed whenever you divide under a prime modulus.

## Where people go wrong

- **Computing the gcd of the whole array.** The question asks specifically for gcd(smallest, largest). It is a reading test.
- **Recursion depth.** The iterative form is trivially safe; the recursive one is fine too since depth is O(log n).
- **gcd(0, x).** It is x, and the loop handles it naturally — but be aware if your inputs can be 0.
- **lcm overflow.** `a * b // gcd` can overflow in fixed-width languages; `a // gcd * b` cannot.

## The reusable template

```python
# Euclid - iterative, O(log min(a,b))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = a // gcd(a, b) * b        # divide FIRST - avoids overflow

# extended Euclid gives x, y with ax + by = gcd(a,b) -> modular inverse.
# modulus is prime? inverse of a is pow(a, p - 2, p).
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| gcd of the entire array | Fold: `reduce(gcd, nums)`. Fast, because the running gcd collapses to 1 quickly. |
| **GCD of Strings** (LC 1071) | The same algebra on strings. Also in your repo. |
| **Insert GCDs in a Linked List** (LC 2807) | Euclid applied at every adjacent pair. Also in your repo. |
| Modular inverse | Extended Euclid, or Fermat’s little theorem when the modulus is prime: `pow(a, p-2, p)`. |
| **Subsequences with equal GCD** (LC 3336) | DP over gcd values. Also in your repo, and much harder. |

## How to think about it next time

Keep a small number-theory toolkit ready: **Euclid** for gcd, **lcm via gcd**, **sieve** for primes up to n, **fast modular exponentiation** for powers under a modulus, and **Fermat** for inverses mod a prime. Five short functions. They turn up constantly in contest-style problems, and the difference between recalling them instantly and re-deriving them is often the difference between finishing and not.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array)
