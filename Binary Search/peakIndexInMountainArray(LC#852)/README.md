# Peak Index in a Mountain Array 🏔️

## Problem Statement

You are given an array `arr` of distinct integers, where `arr` is guaranteed to be a mountain array. A mountain array is defined as an array that:
- Has a length of at least 3.
- There exists an index `i` (0-indexed) with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i-1] < arr[i]`
  - `arr[i] > arr[i+1] > ... > arr[arr.length - 1]`

Return the index of the peak element in the mountain array.

## Approach 🛠️

I've implemented a binary search-based approach to find the peak index in the mountain array.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I performed a binary search in the array to find the peak element.
3. In each iteration of the binary search:
   - I calculated the middle index, `m`, using `(l + r) // 2`.
   - I checked if the element at index `m` is greater than its neighbors.
   - If true, I returned `m` as the peak index.
   - If the element at index `m` is less than its right neighbor, I searched in the right half.
   - If the element at index `m` is less than its left neighbor, I searched in the left half.
4. The loop continues until `l` becomes greater than `r`.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the array `arr`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
