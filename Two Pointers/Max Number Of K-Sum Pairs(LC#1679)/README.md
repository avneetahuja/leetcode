# Max Number of K-Sum Pairs

## Problem Statement

You are given an integer array `nums` and an integer `k`. In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

## Approach 🌟

To solve this problem, we can use a two-pointer approach along with sorting the array:

1. Sort the `nums` array in non-decreasing order.
2. Initialize two pointers `l` and `r` to the start and end of the array, respectively, and set a variable `c` to count the number of operations.
3. Iterate through the array while `l < r`:
   - If the sum of `nums[l]` and `nums[r]` is less than `k`, increment `l`.
   - If the sum is greater than `k`, decrement `r`.
   - If the sum is equal to `k`, increment `c`, increment `l`, and decrement `r`.
4. After iterating through the array, return the value of `c`, which represents the maximum number of operations.

## Complexity Analysis ⚙️

- Time Complexity: O(n log n), where n is the length of the `nums` array.
  - Sorting the array takes O(n log n) time.
  - The two-pointer traversal takes O(n) time.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
