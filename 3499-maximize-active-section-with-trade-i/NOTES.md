# 3499. Maximize Active Section With Trade I
> **Medium** &nbsp;·&nbsp; Run-length scan · pair of adjacent runs &nbsp;·&nbsp; family: **Prefix sums & intervals**

Once you decode what the trade actually does — merge two zero-runs separated by one block of ones — the code is a single pass keeping the previous and current run lengths.

**▶ [Step through this solution line by line](../visualizations/3499-maximize-active-section-with-trade-i.html)** — 15 steps, traced on `s = "1001010"`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

**Think in runs, not characters.** A binary string is a sequence of alternating runs, and most operations on it are really operations on adjacent runs. Here the trade sacrifices one run of 1s to light up the zero-runs on either side of it, so the answer is the baseline plus the best adjacent zero-run pair.

## How to recognise it

- Binary strings or arrays where the question is about blocks, groups, or consecutive stretches.
- Operations described as flipping, merging, or removing a block.
- Whenever you catch yourself writing nested loops over positions, ask whether a single pass over *runs* answers it.

## Where people go wrong

- **Forgetting the trailing run.** Lines 22–24 exist because a zero-run at the very end of the string never triggers the "we just hit a 1" branch. Nearly every run-scanning bug is this one.
- **The `previousZeros = -1` sentinel.** It distinguishes "no previous run yet" from "a previous run of length 0", and using 0 instead would allow an illegal merge at the start.
- **Only resetting `currentZeros` when you see a 1 following zeros.** The `else if (currentZeros > 0)` guard means consecutive 1s do not reset the pairing — which is correct, since only ONE block of ones may be traded.
- **Trying to simulate the trade.** O(n²). Decoding what the trade means is the whole problem.

## The reusable template

```python
# scan RUNS, not characters. keep the previous and current run.
prev, cur, best = -1, 0, 0        # -1 = "no previous run yet" (not 0!)
for c in s:
    if c == '0':
        cur += 1
    elif cur > 0:                 # a zero-run just ended
        if prev != -1:
            best = max(best, prev + cur)
        prev, cur = cur, 0

if cur > 0 and prev != -1:        # TAIL: the string ended mid-run
    best = max(best, prev + cur)

return active + best
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3501) | Larger constraints and a subtler trade rule; you need prefix structures over runs. |
| **Max Consecutive Ones III** (LC 1004) | Flip at most k zeros — a sliding window, not a run scan. |
| Longest run of equal characters | A single run scan, keeping the maximum length. |
| **Longest Subarray With Max Bitwise AND** (LC 2503) | Also a run problem. Also in your repo. |

## How to think about it next time

For binary or categorical sequences, **compress to run-length encoding in your head first**: "1001010" is 1×one, 2×zero, 1×one, 1×zero, 1×one, 1×zero, 1×one. Most operations then become simple statements about neighbouring runs, and the O(n²) simulation you were about to write collapses into a single pass. And always, always check what happens when the sequence ends mid-run.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/maximize-active-sections-with-trade-i)
