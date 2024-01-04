# Count Rotations in Sorted Rotated Array 🔄

## Problem Statement

Given a sorted rotated array of distinct integers `nums`, find the count of rotations, i.e., the index of the minimum element in the rotated array.

## Approach 🛠️

I've implemented a binary search approach to find the index of the minimum element, which represents the count of rotations.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I performed a binary search to find the minimum element index (count of rotations).
3. In each iteration, I calculated the middle index, `mid`, using `(l + r) // 2`.
4. I compared the element at index `mid` with the element at index `mid - 1`. If `nums[mid - 1] > nums[mid]`, then `mid` is the index of the minimum element, and I returned it.
5. If the element at index `l` is less than or equal to the element at index `mid`, I updated `l = mid + 1` to search in the right half.
6. If the element at index `l` is greater than the element at index `mid`, I updated `r = mid - 1` to search in the left half.
7. The loop continues until `l` becomes greater than `r`.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
