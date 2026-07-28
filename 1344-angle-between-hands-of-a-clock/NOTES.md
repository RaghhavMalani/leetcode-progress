# 1344. Angle Between Hands of a Clock
> **Medium** &nbsp;&middot;&nbsp; Math · modular geometry &nbsp;&middot;&nbsp; family: **Math & number theory**

No algorithm at all — just three facts. 30° per hour, **0.5° per minute of hour-hand drift**, 6° per minute. The drift term is what people forget.

**▶ [Step through this solution line by line](./visualization.html)** — 5 steps, traced on `hour = 12, minutes = 30`.

| | |
|---|---|
| time | O(1) |
| space | O(1) |

## The idea

Model each hand as an **angle measured from 12 o’clock**, then the answer is a difference on a circle. Two modelling decisions carry everything: the hour hand moves continuously (0.5°/min), and "the angle between" on a circle means `min(d, 360 − d)`.

## How to recognise it

- Anything circular — clocks, compass bearings, angles, cyclic buffers. The two tools are always `%` for wrapping and `min(d, period − d)` for shortest distance.
- Constant-time closed-form problems: the "algorithm" is the modelling, so spend your time there.

## Where people go wrong

- **Treating the hour hand as static.** At 3:30 it is NOT at 90° — it is at 105°, halfway to 4. This is the bug the problem exists to catch.
- **Forgetting `hour % 12`.** 12:00 must be 0°.
- **Returning the raw difference.** At 12:30 the raw difference is 165°, and that happens to be the smaller one — but at 12:50 it is 275° and the answer is 85°. Always take the min.
- **Integer division.** `minutes * 0.5` must stay a float; `minutes // 2` loses the half degree on odd minutes.

## The reusable template

```python
# model each hand as degrees clockwise from 12, then wrap
hour %= 12
hour_angle   = hour * 30 + minutes * 0.5    # 0.5 deg/min DRIFT - do not omit
minute_angle = minutes * 6

d = abs(hour_angle - minute_angle)
return min(d, 360 - d)                       # shortest arc on a circle

# general circular distance with period p:  min(d, p - d)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Angle at a given number of seconds | Add a seconds term to all three hands: seconds contribute to the minute hand too. |
| When are the hands exactly overlapping? | Solve 30h + 0.5m = 6m for m — every 65 5/11 minutes. |
| Compass bearing difference | Identical `min(d, 360 − d)`. |
| Circular array distance | `min(|i−j|, n − |i−j|)` — the same formula with period n. |

## How to think about it next time

For closed-form problems, **write the model down in words before touching code**: "the hour hand is at 30·h + 0.5·m degrees clockwise from 12". Once the sentence is right the code is one line, and once it is wrong no amount of debugging helps. Also add `min(d, period − d)` to your permanent toolkit — it is the answer to "shortest distance on a circle" in every setting.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock)
