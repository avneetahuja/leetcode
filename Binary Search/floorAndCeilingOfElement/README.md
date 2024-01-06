# Floor and Ceiling of an Element in Sorted Array 🔄

## Problem Statement

Given a sorted array `nums` and a target element, find the floor and ceiling of the target element. The floor and ceiling are the greatest element in the array that is less than or equal to the target, and the smallest element in the array that is greater than or equal to the target, respectively.

## Approach 🛠️

I've implemented a binary search-based approach to find the floor and ceiling of the target element in the sorted array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I performed a binary search to find the floor and ceiling of the target element.
3. In each iteration, I calculated the middle index, `m`, using `(l + r) // 2`.
4. If the element at index `m` is equal to the target, I returned `[nums[m], nums[m]]` as both the floor and ceiling.
5. If the element at index `m` is less than the target, I searched in the right half.
6. If the element at index `m` is greater than the target, I searched in the left half.
7. The loop continues until `l` becomes greater than `r`.
8. The final result is the floor and ceiling of the target element.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
