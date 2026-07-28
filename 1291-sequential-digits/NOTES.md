# 1291. Sequential Digits
> **Medium** &nbsp;&middot;&nbsp; Generate the small candidate set, then filter &nbsp;&middot;&nbsp; family: **Greedy**

The whole problem is realising there are only 36 sequential-digit numbers in existence. Generate all of them from the string "123456789" and filter — the range never enters the loop.

**▶ [Step through this solution line by line](./visualization.html)** — 45 steps, traced on `low = 100, high = 300`.

| | |
|---|---|
| time | O(36 log 36) = O(1) |
| space | O(1) |

## The idea

**Generate, do not search.** When the set of objects with a property is tiny and easy to enumerate, build it directly rather than scanning the input range and testing each candidate. Here the range can span 10⁹ values but only 36 of them can possibly qualify.

## How to recognise it

- A very restrictive structural property (sequential digits, palindromes of fixed length, powers of 2, perfect squares).
- A huge search range with a tiny answer set — the ratio is the signal.
- Ask: **how many objects with this property exist at all?** If the answer is small, enumerate them.

## Where people go wrong

- **Looping from low to high.** Up to 10⁹ iterations. This is the trap the problem is set to catch.
- **Forgetting to sort.** Generating by length gives 12, 23, …, 89, 123, … which is sorted *within* each length but not overall. Actually here it is globally sorted since longer means bigger — but relying on that without saying so is luck, and the sort costs nothing.
- **Off-by-one in `start + len <= 9`.** The substring must fit inside the 9 digits.
- **Starting at len = 1.** The problem requires at least two digits.

## The reusable template

```python
# generate the whole candidate set (only 36 of them), then filter
DIGITS = "123456789"
ans = []
for length in range(2, 10):
    for start in range(0, 10 - length):      # start + length <= 9
        num = int(DIGITS[start:start + length])
        if low <= num <= high:
            ans.append(num)
return sorted(ans)

# the move: when the PROPERTY is restrictive and the RANGE is huge,
# enumerate the property, not the range.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Palindromes in a range | Generate by building half the number and mirroring it — the same "generate, do not search" move. |
| Numbers that are powers of 2 in a range | About 30 of them below 10⁹. |
| **Sequential digits descending too** | Also enumerate substrings of "9876543210". |
| Very large ranges with a dense property | Now you genuinely need digit DP — see LC 3753 in your repo. |

## How to think about it next time

When a problem gives a wide range and a narrow property, always ask **"how many objects satisfy this property in total?"** If the count is small, enumerate them and forget the range. If it is large, you need digit DP or a mathematical characterisation. That single question separates the two solution families cleanly, and choosing wrongly costs you the whole problem.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/sequential-digits)
