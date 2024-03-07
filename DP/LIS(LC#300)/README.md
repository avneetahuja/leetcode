# Longest Increasing Subsequence 📈

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest increasing subsequence.

A subsequence is a sequence of numbers in which each element in the sequence is not necessarily adjacent but is in the same order as the array.

## Approach 📈

This problem can be solved using a dynamic programming approach. We can define a function `lengthOfLIS(i)` that represents the length of the longest increasing subsequence ending at index `i`.

### Steps:
1. Initialize an array `v` with all elements set to 1, representing the length of the LIS ending at each index.
2. Iterate over the array from right to left (starting from the second-to-last element).
3. For each index `i`, iterate over the elements to the right of `i`.
4. If `nums[i] < nums[j]`, update `v[i]` to be the maximum of its current value and `1 + v[j]`.
5. Return the maximum value in the array `v`.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2)
  - The nested loop iterates over all pairs of indices, contributing to the time complexity.
- Space Complexity: O(n)
  - We use additional space to store the lengths of the LIS ending at each index.

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        v = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    v[i] = max(v[i], 1 + v[j])
        return max(v)
