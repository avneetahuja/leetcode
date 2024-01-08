# Search in Rotated Sorted Array 🔄🔍

## Problem Statement

You are given an array of integers that is sorted in ascending order and then rotated.

Your task is to find the index of the target element in the rotated array.

## Approach 🛠️

I've implemented a binary search-based approach to efficiently find the target element in the rotated array.

1. I performed a binary search to find the index where the rotation occurs in the array.
2. Once I found the index of rotation (`minIndex`), I performed two binary searches:
   - One on the left side of the rotation index.
   - Another on the right side of the rotation index.

## Complexity Analysis ⚙️

- Time Complexity: O(log(n)), where n is the number of elements in the array.
  - The binary search is performed twice: once to find the rotation index and then on one side of the rotation index.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
