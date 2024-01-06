# Find Peak Element 🔝

## Problem Statement

You are given an integer array `nums`, where `nums[i] ≠ nums[i+1]` for all valid `i`. A peak element is an element that is strictly greater than its neighbors.

Implement a function to find the index of the peak element. If there are multiple peak elements, return any of them.

## Approach 🛠️

I've implemented a binary search-based approach to find a peak element in the array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I performed a binary search in the array to find a peak element.
3. In each iteration of the binary search:
   - I calculated the middle index, `m`, using `(l + r) // 2`.
   - I checked if the element at index `m` is greater than its neighbors.
   - If true, I returned `m` as a peak element.
   - If the element at index `m` is less than its right neighbor, I searched in the right half.
   - If the element at index `m` is less than its left neighbor, I searched in the left half.
4. The loop continues until `l` becomes greater than `r`.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
