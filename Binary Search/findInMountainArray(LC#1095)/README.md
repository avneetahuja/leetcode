# Find in Mountain Array 🔍⛰️

## Problem Statement

You are given a mountain array, an array that:
- Has a length of at least 3.
- There exists an index `i` (0-indexed) such that:
  - The elements in the array strictly increase from the first element to the `i-th` element.
  - The elements in the array strictly decrease from the `i-th` element to the last element.

You are also given an integer `target`. Your task is to find the index of `target` in the mountain array.

## Approach 🛠️

I've implemented a binary search-based approach to find the target in the mountain array.

1. I used binary search to find the peak element in the mountain array.
2. Once the peak is found, I performed binary search in the increasing and decreasing parts of the array separately.
3. If the target is found in either part, I returned the corresponding index.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the mountain array.
  - The binary search is performed twice, once for finding the peak and once for finding the target in either the increasing or decreasing part.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
