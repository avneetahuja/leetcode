# Partition Equal Subset Sum Dynamic Programming 🎯🧩

## Problem Statement

Given an array of integers `nums`, the task is to determine whether it's possible to divide the array into two non-empty subsets with the same sum.

## Approach 🛠️

The solution uses dynamic programming to check if there exists a subset with a sum equal to half of the total sum of the array.

1. **Checking for Valid Sum:**
   - If the total sum of the array is not even, return `False` since it's not possible to divide into two subsets with equal sum.

2. **Subset Sum Dynamic Programming Function (`subsetSum`):**
   - Create a 2D array `t` to store intermediate results, where `t[i][j]` indicates whether there exists a subset with sum `j` in the first `i` elements of the array.
   - Initialize the table with `True` for the entire first column (`t[i][0] = True`), indicating that an empty subset always has a sum of 0.

3. **Filling the Dynamic Programming Table:**
   - Iterate over each element in the array (`nums[i]`) and each possible sum (`j`) in the range of the table dimensions.
   - Update `t[i][j]` based on the recurrence relation:
     - If `nums[i-1] <= j`, set `t[i][j]` to `True` if either the subset with sum `j-nums[i-1]` exists (`t[i-1][j-nums[i-1]]`) or the subset without including the current element exists (`t[i-1][j]`).
     - If `nums[i-1] > j`, set `t[i][j]` to `t[i-1][j]`.

4. **Final Result:**
   - The result is `True` if there exists a subset with a sum equal to half of the total sum (`t[len(nums)][sum(nums)//2]`), and `False` otherwise.

## Complexity Analysis ⚙️

The time complexity of the solution is O(len(nums) * sum(nums)), and the space complexity is also O(len(nums) * sum(nums)) due to the dynamic programming table.
