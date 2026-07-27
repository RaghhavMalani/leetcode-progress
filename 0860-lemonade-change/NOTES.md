# 860. Lemonade Change
> **Easy** &nbsp;·&nbsp; Greedy · spend the least flexible resource first &nbsp;·&nbsp; family: **Greedy**

Only one line in this problem is a real decision: paying $15 with a $10 + $5 rather than three $5s. The reason is that $5 notes are more flexible, so you hoard them.

**▶ [Step through this solution line by line](../visualizations/0860-lemonade-change.html)** — 18 steps, traced on `bills = [5,5,10,10,20]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

The greedy rule is **spend your least flexible resource first**. A $10 note can only ever be used as change for a $20; a $5 can be used for a $10 *or* a $20. So whenever both options exist, use the $10 and keep the $5s. An exchange argument proves it: any successful strategy that used three $5s where a $10 was available can be rewritten to use the $10, and it remains successful.

## How to recognise it

- Resource allocation where the resources have different **usefulness ranges**.
- The word "greedy" is justified only when you can name the exchange argument. Here you can, in one sentence.
- Similar: assigning tasks to machines, giving change with coins, allocating rooms — always ask which resource is the constrained one.

## Where people go wrong

- **Preferring three $5s for a $20.** It passes many tests and fails on inputs where a later $10 customer needs a $5.
- **Tracking $20 notes.** They are never useful as change — you never give change larger than $15 — so counting them is pointless.
- **Assuming you can start with change.** You cannot; the first customer must pay $5.
- **Not justifying the greedy.** The exchange argument takes ten seconds and is what the problem is actually testing.

## The reusable template

```python
# spend the LEAST FLEXIBLE resource first
five = ten = 0
for bill in bills:
    if bill == 5:
        five += 1
    elif bill == 10:
        if not five: return False
        five -= 1; ten += 1
    else:                          # 20 -> owe 15
        if ten and five:           # PREFER 10+5: a $10 is useless elsewhere
            ten -= 1; five -= 1
        elif five >= 3:
            five -= 3
        else:
            return False
return True
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Arbitrary coin denominations | Greedy fails in general — the classic counterexample is coins {1, 3, 4} making 6. You need DP. |
| Minimise the number of notes given | Coin change DP. |
| **Maximum Ice Cream Bars** (LC 1833) | Greedy by cheapest first. Also in your repo. |
| Unlimited change available | Trivially always true — the whole problem is the scarcity. |

## How to think about it next time

When several resources can satisfy a demand, rank them by **how many future demands each could serve** and spend the most specialised one first. That is the same principle behind "assign the tightest-deadline job first" and "use the largest coin that still fits". And always pair a greedy with its exchange argument — "swapping to the greedy choice never makes the outcome worse" — because a greedy you cannot justify is a greedy you will apply in the wrong place.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/lemonade-change)
