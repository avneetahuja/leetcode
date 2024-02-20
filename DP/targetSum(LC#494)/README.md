# Target Sum Ways 🎯

## Problem Statement

Given an array `nums` of length `n` and an integer `target`, find the number of ways to assign symbols to each array element such that the sum is equal to the target.

Each element of the array must be assigned either the positive or negative symbol. The number of ways to assign symbols to make the sum equal to the target is returned.

## Approach 🛠️

To find the number of ways to achieve the target sum, the problem can be mapped to finding the count of subsets with a given sum. The target sum (`target`) is converted into a sum (`s1`) for subsets of the array. The count of subsets with the sum `s1` is then calculated using dynamic programming.

1. **Subset Sum Count DP:**
   - Create a 2D array `t` with dimensions `(n+1) x (s1+1)` and initialize it to zero.
   - Set the base case where the sum is 0 for any number of elements: `t[i][0] = 1` for all `i`.
   - Iterate through the array elements and the sum:
     - If the current element is less than or equal to the current sum, update `t[i][j]` using the subset sum count formula.
     - Otherwise, copy the count from the previous row: `t[i][j] = t[i-1][j]`.
   - The final answer is stored in `t[n][s1]`.

## Complexity Analysis ⚙️

- The time complexity is O(n * s1), where n is the length of the array and s1 is the target sum.
- The space complexity is O(n * s1) as well, as the solution uses a 2D array for dynamic programming.
