# Count Subsets with Given Difference Dynamic Programming 🔢✨

## Problem Statement

Given an array of positive integers `arr`, find the count of subsets with a given difference `target`.

## Approach 🛠️

The solution uses dynamic programming to count subsets with a given difference.

1. **Subset Count Dynamic Programming Function (`countSubsetsWithGivenDifference`):**
   - Create a 2D array `t` to store intermediate results, where `t[i][j]` represents the count of subsets in the first `i` elements of the array with a sum of `j`.
   - Initialize the table with `1` for the entire first column (`t[i][0] = 1`), indicating that there is one subset with a sum of 0 (the empty subset).

2. **Filling the Dynamic Programming Table:**
   - Iterate over each element in the array (`arr[i]`) and each possible sum (`j`) in the range of the table dimensions.
   - Update `t[i][j]` based on the recurrence relation:
     - If `arr[i-1] <= j`, set `t[i][j]` to the sum of counts with and without including the current element (`t[i-1][j-arr[i-1]] + t[i-1][j]`).
     - If `arr[i-1] > j`, set `t[i][j]` to `t[i-1][j]`.

3. **Counting Subsets with the Given Difference:**
   - Calculate the target sum (`s1`) as `(target + sum(arr)) // 2`.
   - Return `t[len(arr)][s1]`, which represents the count of subsets with the required difference.

4. **Output:**
   - The function prints the dynamic programming table `t` for illustration purposes.

## Complexity Analysis ⚙️

The time complexity of the solution is O(n * s1), where n is the length of the array and s1 is the target sum. The space complexity is also O(n * s1) due to the dynamic programming table.
