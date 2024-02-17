# Subarray Sum Equal to Sum Dynamic Programming 🧩🔍

## Problem Statement

Given an array of integers `arr` and an integer `sum`, the task is to check if there exists a subarray with a sum equal to the given `sum`.

## Approach 🛠️

The solution uses dynamic programming to check for the presence of a subarray with the desired sum.

1. **Dynamic Programming Table (`t`):**
   - Create a 2D array `t` with dimensions `(len(arr) + 1) x (sum + 1)` to store intermediate results.
   - Initialize the table with `True` for the entire first column (`t[i][0] = True`), indicating that a subarray with sum 0 always exists.

2. **Filling the Dynamic Programming Table:**
   - Iterate over each element in the array (`arr[i]`) and each possible sum (`j`) in the range of the table dimensions.
   - Update `t[i][j]` based on the recurrence relation:
     - If `arr[i-1] <= j`, set `t[i][j]` to `True` if either the subarray with sum `j-arr[i-1]` exists (`t[i-1][j-arr[i-1]]`) or the subarray without including the current element exists (`t[i-1][j]`).
     - If `arr[i-1] > j`, set `t[i][j]` to `t[i-1][j]`.

3. **Final Result:**
   - The result is stored in `t[len(arr)][sum]`, indicating whether there exists a subarray with the given sum.

## Complexity Analysis ⚙️

The time complexity of the solution is O(len(arr) * sum), and the space complexity is also O(len(arr) * sum) due to the dynamic programming table.

Feel free to adapt the code for your specific use case.
