# Burst Balloons 🎈💥

## Problem Statement

You are given `n` balloons indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst balloon `i`, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

## Approach 🎈

(Memoisation)
This problem can be solved using a dynamic programming approach. We can define a recursive function `f(i, j)` that represents the maximum coins that can be collected by bursting balloons between indices `i` and `j` (inclusive).

### Steps:
1. Initialize a 2D array `t` to store the results of subproblems. Set all entries to -1 to indicate that the result is not yet calculated.
2. Define the recursive function `f(i, j)` that calculates the maximum coins by considering the options to burst balloons between indices `i` and `j`.
   - If `i > j`, return 0.
   - If `t[i][j]` is not -1, return `t[i][j]`.
   - For each balloon `ind` between indices `i` and `j` (inclusive), calculate the cost of bursting the balloon at `ind` and recursively call the function for the remaining subproblems. Update the maximum cost.
3. Call the recursive function with the initial parameters `f(0, n-1)` to start the process from the first and last balloons.
4. Return the result.

## Complexity Analysis ⚙️

- Time Complexity: O(n^3)
  - The recursive function is called for each possible subarray of balloons.
- Space Complexity: O(n^2)
  - We use additional space for memoization in the 2D array.

