# Find Minimum in Rotated Sorted Array 🔄

## Problem Statement

Suppose an array of length `n` is rotated between `1` and `n - 1` times. Given the rotated sorted array `nums`, return the minimum element.

## Approach 🛠️

I've implemented a binary search-based approach to find the minimum element in the rotated sorted array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I checked if the array is not rotated by comparing the first and last elements. If not, I returned `nums[0]`.
3. I performed a binary search to find the minimum element in the rotated array.
4. In each iteration, I calculated the middle index, `m`, using `(l + r) // 2`.
5. If the element at index `m` is less than the element at index `m - 1`, I returned `nums[m]` as the minimum element.
6. If the element at index `m` is greater than the element at index `r`, I searched in the right half.
7. If the element at index `m` is less than or equal to the element at index `r`, I searched in the left half.
8. The loop continues until `l` becomes greater than `r`.
9. The final result is the minimum element in the rotated sorted array.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
