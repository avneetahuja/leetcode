# Maximum Sliding Window 🔄

## Problem Statement

Given an array `nums` of integers and an integer `k`, find the maximum value in each window of size `k` as it slides through the array.

**Example:**
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: The maximum value in each window of size 3 is [3, 3, 5, 5, 6, 7].

## Approach 🛠️

I've used a Python class-based solution to find the maximum value in each sliding window.

1. I initialized two pointers `i` and `j` to represent the start and end of the current window.
2. I used a list `listt` to store elements that might be the maximum in the current window.
3. I initialized an empty list `res` to store the result.
4. I iterated through the array `nums` using the pointers `i` and `j`.
5. While the current element `nums[j]` is greater than the last element in `listt`, I removed elements from `listt` until it becomes empty or the last element is greater than the current element.
6. I appended the current element `nums[j]` to `listt`.
7. If the size of the current window `(j - i + 1)` is less than `k`, I expanded the window by incrementing `j`.
8. When the size of the window reaches `k`, I added the maximum element in the current window to the result list and adjusted `listt` accordingly.
9. I moved the window by incrementing `i` and `j`.
10. The function returned the list of maximum values in each sliding window.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(k), where k is the size of the sliding window.
  - The space used by the `listt` list.
