# Longest Subarray of 1's After Deleting One Element

## Problem Statement

Given a binary array `nums`, you should delete one element from it. Return the length of the longest subarray containing only 1's in the resulting array after performing at most one deletion.

## Approach 🌟

We can use a sliding window approach to find the length of the longest subarray of 1's after deleting at most one element.

1. Initialize two pointers `l` and `r` to traverse the array `nums`.
2. Move the right pointer `r` until we reach the end of the array.
3. If `nums[r]` is 0, increment the count of zeros `current_count`.
4. If `current_count` is less than or equal to 1, update the maximum length of consecutive 1's encountered so far.
5. If `current_count` exceeds 1, move the left pointer `l` until the count of zeros `current_count` becomes less than or equal to 1. This is done by incrementing `l` until `nums[l]` becomes 1.
6. Update the maximum length of consecutive 1's encountered so far.
7. Repeat steps 2-6 until the right pointer `r` reaches the end of the array.
8. Return the maximum length of consecutive 1's encountered minus 1.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`. Both the left and right pointers traverse the array at most once.
- Space Complexity: O(1), as we only use a constant amount of extra space.
