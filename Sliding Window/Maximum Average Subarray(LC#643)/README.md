# Maximum Average Subarray of Length K

## Problem Statement

Given an array `nums` and an integer `k`, find the contiguous subarray of size `k` with the maximum average value and return this maximum average value as a float.

## Approach 🌟

To solve this problem, we can use a sliding window approach.

1. Initialize variables `l`, `r`, `n`, `cur_sum`, and `max_sum`.
   - `l`: Left pointer of the sliding window.
   - `r`: Right pointer of the sliding window.
   - `n`: Length of the array `nums`.
   - `cur_sum`: Current sum of elements inside the sliding window.
   - `max_sum`: Maximum sum found so far.

2. Iterate over the array `nums` using the right pointer `r`.
   - If the size of the sliding window is less than `k`, add the current element `nums[r]` to `cur_sum`.
   - If the size of the sliding window becomes equal to `k`, update `max_sum` with the maximum of `max_sum` and `cur_sum`, then move the window by subtracting `nums[l]` from `cur_sum` and incrementing `l`.

3. After the iteration, return `max_sum / k`, which represents the maximum average subarray of length `k`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - We perform a single pass over the array `nums` with two pointers.
- Space Complexity: O(1).
  - We use only a constant amount of extra space for storing variables.
