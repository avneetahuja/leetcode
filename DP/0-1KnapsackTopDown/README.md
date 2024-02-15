# 0/1 Knapsack Dynamic Programming (Top-Down) 🎒💰

## Problem Statement

You are given weights and values of items and a knapsack capacity. The goal is to find the maximum value that can be obtained by selecting a subset of the items such that the sum of their weights is less than or equal to the knapsack capacity.

## Approach 🛠️

The solution uses dynamic programming (Top-Down) to solve the 0/1 Knapsack Problem.

1. **Dynamic Programming Table (`t`):**
   - Create a 2D array `t` with dimensions `(size + 1) x (capacity + 1)` to store intermediate results.
   - Initialize the table with 0 for the first row (when there are no items) and 0 for the first column (when the capacity is 0).

2. **Filling the Dynamic Programming Table:**
   - Iterate over each item (`i`) and each capacity (`j`) in the range of the table dimensions.
   - If the weight of the current item is less than or equal to the current capacity (`weights[i-1] <= j`), update `t[i][j]` by taking the maximum of two cases:
     - Including the current item and reducing the capacity by the weight of the current item: `values[i-1] + t[i-1][j-weights[i-1]]`
     - Excluding the current item: `t[i-1][j]`
   - If the weight of the current item is greater than the current capacity, update `t[i][j]` by copying the value from the row above: `t[i][j] = t[i-1][j]`

3. **Final Result:**
   - The result is stored in `t[size][capacity]`, representing the maximum value that can be obtained.

## Complexity Analysis ⚙️

The time complexity of the solution is O(size * capacity), where size is the number of items and capacity is the knapsack capacity. The space complexity is also O(size * capacity) due to the dynamic programming table.

The solution uses dynamic programming to avoid redundant calculations and improve the time complexity.
