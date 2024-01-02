# Binary Search 🔍

## Problem Statement

Given a sorted array of integers `nums` and a target value, implement a binary search algorithm to find the target's index if it exists in the array. If the target is not found, return -1.

## Approach 🛠️

I've used a standard binary search approach to efficiently find the target in the sorted array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I iterated through the array while `l` was less than or equal to `r`.
3. In each iteration, I calculated the middle index, `mid`, using `(l + r) // 2`.
4. I compared the target with the element at index `mid`:
   - If they are equal, I returned `mid` as the target is found.
   - If the target is less than the element at `mid`, I updated `r = mid - 1` for the left half search.
   - If the target is greater than the element at `mid`, I updated `l = mid + 1` for the right half search.
5. If the loop completes without finding the target, I returned -1.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
