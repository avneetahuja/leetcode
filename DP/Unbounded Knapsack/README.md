# Unbounded Knapsack Top-Down Approach 🎒🔄

## Problem Statement

Given weights and values of `n` items, put these items in a knapsack of unlimited capacity to get the maximum total value in the knapsack.

## Approach 🛠️

The problem can be solved using dynamic programming. The top-down approach is utilized in this solution.

1. **Initialize 2D Array:**
   - Create a 2D array `t` with dimensions `(size+1) x (capacity+1)` and initialize it to `-1` to represent unexplored subproblems.
   - The rows represent the items, and the columns represent the remaining capacity of the knapsack.

2. **Base Case:**
   - Set the base case where either the number of items is 0 or the capacity is 0: `t[i][0] = 0` and `t[0][j] = 0` for all `i` and `j`.

3. **Fill the Array:**
   - Iterate through the items and the remaining capacity.
   - If the weight of the current item is less than or equal to the remaining capacity, update `t[i][j]` using the maximum of including or excluding the current item.
   - Otherwise, copy the value from the previous row: `t[i][j] = t[i-1][j]`.

4. **Result:**
   - The final answer is stored in `t[size][capacity]`.

## Complexity Analysis ⚙️

- Time Complexity: O(size * capacity), where `size` is the number of items and `capacity` is the capacity of the knapsack.
- Space Complexity: O(size * capacity) for the 2D array used in dynamic programming.
