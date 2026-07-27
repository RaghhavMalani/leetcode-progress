# 3020. Find the Maximum Number of Elements in a Subset
> **Medium** &nbsp;·&nbsp; Frequency map · chain following &nbsp;·&nbsp; family: **Hashing**

The pattern x, x², x⁴, … and back down. Two things make it tractable: repeated squaring blows past 10⁹ in about five steps, and 1 needs its own case because 1² = 1.

**▶ [Step through this solution line by line](../visualizations/3020-find-the-maximum-number-of-elements-in-subset.html)** — 16 steps, traced on `nums = [5,4,1,2,2]`.

| | |
|---|---|
| time | O(n log log maxValue) — the chain from any x has at most ~5 links |
| space | O(n) |

## The idea

A **chain-following** problem. Build a frequency map, then from each starting value walk a deterministic successor function (here x → x²) while the required multiplicities exist. The chains are short because squaring grows doubly exponentially, which is what keeps a nested loop nearly linear.

## How to recognise it

- A required arrangement defined by a recurrence on values — doubling, squaring, +1, ×k.
- Multiset conditions ("must appear twice") → you need counts, not just membership.
- The related family: LC 128 longest consecutive sequence (successor x+1), LC 954 array of doubled pairs (successor 2x). Same skeleton.

## Where people go wrong

- **Not special-casing 1.** The while loop never terminates, since 1² = 1 and freq[1] stays ≥ 2. This is the bug that hangs your submission.
- **Getting the parity of the 1s wrong.** The pattern length must be odd, so an even count of 1s contributes count − 1.
- **Requiring `freq[cur] >= 2` for the peak.** The peak appears once; only the non-peak elements need two copies. The loop structure handles this because the peak is counted by the initial `length = 1`.
- **Overflow in fixed-width languages.** `cur * cur` with cur near 10⁹ overflows 32 bits — guard it or use 64-bit.

## The reusable template

```python
# frequency map + follow a deterministic successor chain
freq = Counter(nums)
ans = 1

if 1 in freq:                          # FIXED POINT: 1*1 == 1, handle separately
    ones = freq[1]
    ans = max(ans, ones if ones % 2 else ones - 1)   # length must be ODD

for x in freq:
    if x == 1: continue                # or the while below never terminates
    length, cur = 1, x
    while freq[cur] >= 2 and cur * cur in freq:      # need TWO copies (both sides)
        length += 2
        cur *= cur                     # doubly exponential -> ~5 iterations max
    ans = max(ans, length)
return ans
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Longest Consecutive Sequence** (LC 128) | Successor is x+1, and you only start where x−1 is absent. Also in your repo. |
| **Array of Doubled Pairs** (LC 954) | Successor is 2x, matched greedily from the smallest absolute value. |
| Longest chain with x → x·k | Same skeleton, but chains are longer so watch the complexity. |
| Longest arithmetic subsequence | A different beast entirely — DP over (index, difference). |

## How to think about it next time

Two questions for any chain-following problem. **(1) How long can a chain be?** That bounds the inner loop and tells you whether the nested structure is affordable. **(2) Are there fixed points?** Values where successor(x) = x — 1 for squaring, 0 for doubling — cause infinite loops and always need a special case. Asking those two questions up front catches both the complexity concern and the crash.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-a-subset)
