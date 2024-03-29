# Number of Dice Rolls to Target Sum 🎲

## Problem Statement

You have `d` dice, and each die has `f` faces numbered `1, 2, ..., f`.

Return the number of possible ways (out of `f^d` total ways) to roll the dice so the sum of the face-up numbers equals `target`.

Since the answer may be very large, return it modulo `10^9 + 7`.

## Approach 🎯

This problem can be solved using dynamic programming with memoization:

1. Define a recursive function `f(nLeft, s)` to represent the number of ways to achieve sum `s` with `nLeft` dice.
2. Use memoization to avoid redundant computations by storing the results of subproblems in a dictionary `t`.
3. Base cases:
   - If `nLeft` is 0, return 1 if `s` is 0 (indicating a successful roll), otherwise return 0.
4. Recursive case:
   - Iterate through each possible face value of the die (from 1 to `k`).
   - For each face value, recursively call `f(nLeft - 1, s - i)` to compute the number of ways to achieve the remaining sum with `nLeft - 1` dice and `s - i` as the new target sum.
   - Add up the results of all possible rolls.
5. Return the result modulo `10^9 + 7`.

## Complexity Analysis ⚙️

- Time Complexity: O(n * k * target)
  - The function `f(nLeft, s)` is called for each combination of remaining dice (`nLeft`), target sum (`s`), and possible face values (`1` to `k`).
- Space Complexity: O(n * target)
  - We use additional space for memoization in the `t` dictionary.
