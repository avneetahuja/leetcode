# Count of Sum Subsets Dynamic Programming 🎯🧩

## Problem Statement

Given an array of integers `arr` and a target sum `sum`, the task is to count the number of subsets of the array that add up to the given sum.

## Approach 🛠️

The solution uses dynamic programming to count the number of subsets with a sum equal to the target sum.

1. **Subset Sum Dynamic Programming Function (`countSumSubsets`):**
   - Create a 2D array `t` to store intermediate results, where `t[i][j]` indicates whether there exists a subset with sum `j` in the first `i` elements of the array.
   - Initialize the table with `True` for the entire first column (`t[i][0] = True`), indicating that an empty subset always has a sum of 0.

2. **Filling the Dynamic Programming Table:**
   - Iterate over each element in the array (`arr[i]`) and each possible sum (`j`) in the range of the table dimensions.
   - Update `t[i][j]` based on the recurrence relation:
     - If `arr[i-1] <= j`, set `t[i][j]` to `True` if either the subset with sum `j-arr[i-1]` exists (`t[i-1][j-arr[i-1]]`) or the subset without including the current element exists (`t[i-1][j]`).
     - If `arr[i-1] > j`, set `t[i][j]` to `t[i-1][j]`.

3. **Counting the Subsets:**
   - Iterate over each row in the table (`t[i]`) and increment the `count` for each row where `t[i][sum]` is `True`.

4. **Final Result:**
   - The result is the value of `count`, representing the number of subsets with a sum equal to the target sum.

## Complexity Analysis ⚙️

The time complexity of the solution is O(len(arr) * sum) for filling the dynamic programming table, and the space complexity is also O(len(arr) * sum) due to the dynamic programming table.
