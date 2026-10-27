# Minimum-Cost Activity Scheduling for a Cranky Toddler

Project for **Design and Analysis of Algorithms**.

**Authors:** Gedela Sai Shashank (Bmat2414), Gudavalli Sathya Tej (Bmat2415)
**Repository:** https://github.com/SaiShashankG/Kid_Cranky_Time

## Problem

A parent wants to enrol a toddler in online activities. Each activity has a start time, an end time and a fee. The toddler gets cranky at certain times of the day. Choose a set of activities such that

1. the child is enrolled in some activity at **every** cranky time,
2. no two chosen activities overlap, and
3. the **total fee is minimum**.

If no valid schedule exists, the answer is `inf`. If there are no cranky times, the answer is `0`.

## Approach

Sort the activities by end time and solve with dynamic programming over chains of non-overlapping activities. Let `f(i)` be the minimum fee of a valid partial schedule whose last activity is `i`. A precomputed array `nxt[j]` (the first cranky time after activity `j` ends) lets us test in O(1) whether activity `i` can directly follow activity `j`. The final answer is the minimum of `f(i)` over activities that can end the schedule.

| Algorithm | Time | Space |
|---|---|---|
| Brute force (all subsets, correctness oracle) | $O(2^n · n · (m + log n))$ | $O(n)$ |
| Dynamic programming (`optimized.py`) | $O(n² + nm + m log m)$ | $O(n + m)$ |

Here `n` is the number of activities and `m` is the number of cranky times.

## Files

| File | Description |
|---|---|
| `optimized.py` | Efficient DP algorithm, function `schedule_activities(activities, cranky)` |
| `brute_force.py` | Exhaustive-search oracle, function `brute_force(activities, cranky)` |
| `notes.ipynb` | Step-by-step development and the randomised comparison test |
| `report.pdf` | Project report (LaTeX) with the proof of correctness and analysis |

## Requirements

- Python 3.8 or newer
- No external libraries (only the standard library is used)

## How to run

Run each program directly. Each one prints the results for its built-in examples:

```bash
python optimized.py
python brute_force.py
```

Expected output for the three built-in examples:

```
7
9
0
```

To run the randomised test, open `notes.ipynb` in Jupyter and run all cells. It compares the DP against brute force on thousands of random small instances and reports any mismatch.

## Using the functions

```python
from optimized import schedule_activities

# Each activity is (start, end, fee). Times are numbers in one common unit,
# for example minutes after midnight (8:00 AM = 480).
activities = [(480, 600, 5), (510, 570, 3), (630, 690, 4), (480, 720, 20), (690, 750, 1)]

# Cranky times, in the same unit (9:00 AM = 540, 11:00 AM = 660).
cranky = [540, 660]

print(schedule_activities(activities, cranky))   # 7
```

### Input format

- `activities`: a list of `(start, end, fee)` tuples with `start < end` and `fee > 0`.
- `cranky`: a list of times in the same unit as the activities, in any order.

### Output

- The minimum total fee, as a number.
- `0` if `cranky` is empty.
- `inf` (`float('inf')`) if no valid schedule exists.

## Assumptions

- Activities are **closed intervals** `[start, end]`, so a cranky time exactly at an activity's start or end is covered by that activity.
- Two activities that **touch** (`end = start`) do not overlap and can both be chosen.
- Each activity can be chosen at most once, and all fees are positive.

## Author notes

The report explains the algorithm, the proof of correctness and the complexity analysis in full. The brute-force program is used only as a ground-truth oracle for testing the DP on small inputs.
