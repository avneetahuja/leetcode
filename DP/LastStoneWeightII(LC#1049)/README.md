# Last Stone Weight II Dynamic Programming 🪨✨

## Problem Statement

We are given an array of stones, where each stone has a positive integer weight. Each turn, we choose any two stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has a new weight `y - x`.

At the end, there is at most one stone left. Return the smallest possible weight of this stone (the weight is 0 if there are no stones left).

## Approach 🛠️

The solution uses dynamic programming to find the minimum subset sum difference.

1. **Subset Sum Dynamic Programming Function (`lastStoneWeightII`):**
   - Create a 2D array `t` to store intermediate results, where `t[i][j]` indicates whether there exists a subset with sum `j` in the first `i` elements of the array.
   - Initialize the table with `True` for the entire first column (`t[i][0] = True`), indicating that an empty subset always has a sum of 0.

2. **Filling the Dynamic Programming Table:**
   - Iterate over each element in the array (`stones[i]`) and each possible sum (`j`) in the range of the table dimensions.
   - Update `t[i][j]` based on the recurrence relation:
     - If `stones[i-1] <= j`, set `t[i][j]` to `True` if either the subset with sum `j-stones[i-1]` exists (`t[i-1][j-stones[i-1]]`) or the subset without including the current element exists (`t[i-1][j]`).
     - If `stones[i-1] > j`, set `t[i][j]` to `t[i-1][j]`.

3. **Finding the Minimum Subset Sum Difference:**
   - Iterate over possible sums from `s//2` to `0` (inclusive) and return `s - 2 * i` for the first sum `i` where `t[n][i]` is `True`.

4. **Handling Edge Case:**
   - If there is no subset sum difference found, return the weight of the first stone (`stones[0]`).

## Complexity Analysis ⚙️

The time complexity of the solution is O(n * s), where n is the number of stones and s is the sum of weights. The space complexity is also O(n * s) due to the dynamic programming table.
