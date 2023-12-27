# Largest Subarray with Sum K 📈

## Problem Statement

Given an array of integers `nums` and an integer `k`, find the length of the largest subarray with a sum equal to `k`.

**Example:**
Input: nums = [4,1,1,1,2,3,5], k = 5
Output: 4
Explanation: The subarray [1, 1, 1, 2] has a sum of 5, which is the largest subarray with the given sum.


## Approach 🛠️

I've used a sliding window approach to find the length of the largest subarray with a sum equal to `k`.

1. I initialized two pointers, `i` and `j`, representing the start and end of the sliding window.
2. I used a while loop to iterate through the array.
3. I maintained a variable `s` to keep track of the sum of the current subarray.
4. If the sum `s` is less than `k`, I expanded the window by incrementing `j`.
5. If the sum `s` is equal to `k`, I checked if the length of the current subarray is greater than the maximum length `maxL` seen so far.
6. If the sum `s` is greater than `k`, I contracted the window by incrementing `i` until the sum becomes less than or equal to `k`.
7. I updated `maxL` with the maximum length seen so far.
8. I repeated these steps until `j` reaches the end of the array.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through the array once using the sliding window approach.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
