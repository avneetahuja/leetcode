# Search in Infinite Array 🔍

## Problem Statement

You are given an infinite sorted array. Implement a function to find the index of the target element in the array. If the target element is not present in the array, return -1.

## Approach 🛠️

I've implemented a binary search-based approach to find the index of the target element in the infinite array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I initialized `r` to an arbitrary large value (e.g., 100) to simulate the infinite array.
3. I checked if the element at index `r` is less than the target. If true, I increased the search space by updating `l` to `r` and further increased `r`.
4. I performed a binary search in the enlarged search space to find the index of the target element.
5. In each iteration of the binary search, I calculated the middle index, `m`, using `(l + r) // 2`.
6. If the element at index `m` is equal to the target, I returned `m`.
7. If the element at index `m` is less than the target, I searched in the right half.
8. If the element at index `m` is greater than the target, I searched in the left half.
9. The loop continues until `l` becomes greater than `r`.
10. If the target element is not found, I returned -1.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the index of the target element.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.

Feel free to customize this README further based on additional details you want to provide or any specific formatting preferences you have.
