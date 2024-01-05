# Search Insert Position 🎯

## Problem Statement

Given a sorted array of distinct integers `nums` and a target value `target`, return the index of `target` if it is present. If not, return the index where it would be if it were inserted in order.

## Approach 🛠️

I've implemented a binary search-based approach to find the index where the target should be inserted.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search.
2. I maintained a variable `floor` to track the potential index where the target should be inserted.
3. I performed a binary search to find the index of the target or the floor index.
4. In each iteration, I calculated the middle index, `m`, using `(l + r) // 2`.
5. If the element at index `m` is equal to the target, I returned `m`.
6. If the element at index `m` is less than the target, I updated `floor = m` and searched in the right half.
7. If the element at index `m` is greater than the target, I updated `r = m - 1` to search in the left half.
8. The loop continues until `l` becomes greater than `r`.
9. I returned `floor + 1` as the final result.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
