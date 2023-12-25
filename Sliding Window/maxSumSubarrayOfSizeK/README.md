# Maximum Sum Subarray of Size K 📈

## Problem Statement

Given an array `nums` of integers and a window size `k`, find the maximum sum of a subarray of size `k`.

**Example:**
Input: nums = [1, 4, 2, 10, 2, 3, 1, 0, 20], k = 4
Output: 28
Explanation: The subarray with the maximum sum of size 4 is [2, 10, 2, 3, 1, 0, 20], and its sum is 28.

markdown
Copy code

## Approach 🛠️

I've used a Python class-based solution to find the maximum sum subarray of size `k`.

1. I initialized two pointers `i` and `j` to represent the start and end of the current subarray.
2. I used a variable `sum` to keep track of the sum of the current subarray and `maxSum` to store the maximum sum encountered so far.
3. I iterated through the array `nums` using the pointers `i` and `j`.
4. While the size of the current subarray `(j - i + 1)` is less than `k`, I expanded the subarray by incrementing `j`.
5. When the size of the subarray reaches `k`, I calculated the sum and updated `maxSum` accordingly.
6. I moved the window by incrementing `i` and `j` and adjusting the sum accordingly.
7. The function returned the maximum sum of a subarray of size `k`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
