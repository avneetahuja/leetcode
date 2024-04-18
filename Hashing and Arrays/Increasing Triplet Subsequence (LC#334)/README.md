# Increasing Triplet Subsequence

## Problem Statement

Given an integer array `nums`, return true if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

## Approach 🌟

We can solve this problem by iterating through the array once. We maintain two variables `A` and `B`. Initially, we set `A` to the first element of the array and `B` to positive infinity. Then, for each element `n` in the array:

1. If `n` is less than `A`, we update `A` to `n`. This ensures that `A` always holds the smallest value encountered so far.
2. If `n` is greater than `A` but less than `B`, we update `B` to `n`. This ensures that `B` holds the second smallest value encountered so far.
3. If `n` is greater than both `A` and `B`, we have found a triplet `(A, B, n)` where `A < B < n`, and we return `true`.
4. If we do not find such a triplet after iterating through the array, we return `false`.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of elements in the array.
  - We iterate through the array once.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
