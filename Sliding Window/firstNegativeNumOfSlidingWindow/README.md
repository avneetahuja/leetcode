# First Negative Integer in Each Sliding Window 🔄

## Problem Statement

Given an array `nums` of integers and an integer `k`, find the first negative integer in each window of size `k` as it slides through the array.

**Example:**
Input: nums = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
Output: [-1, -1, -7, -15, -15, 0]
Explanation: The first negative integer in each window of size 3 is [-1, -1, -7, -15, -15, 0].

markdown
Copy code

## Approach 🛠️

I've used a Python class-based solution to find the first negative integer in each sliding window.

1. I initialized two pointers `i` and `j` to represent the start and end of the current window.
2. I used a list `listt` to store negative integers in the current window and an empty list `res` to store the result.
3. I iterated through the array `nums` using the pointers `i` and `j`.
4. If the current element `nums[j]` is negative, I appended it to `listt`.
5. If the size of the current window `(j - i + 1)` is less than `k`, I expanded the window by incrementing `j`.
6. When the size of the window reaches `k`, I added the first negative integer in the current window to the result list and adjusted `listt` accordingly.
7. If `listt` is empty, it means there is no negative integer in the current window, so I added `0` to the result list.
8. I moved the window by incrementing `i` and `j`.
9. The function returned the list of first negative integers in each sliding window.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(k), where k is the size of the sliding window.
  - The space used by the `listt` list.
