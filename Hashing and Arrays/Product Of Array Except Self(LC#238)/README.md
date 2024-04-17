# Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Approach 🌟

To find the product of all elements except self, we can use a two-pass approach:

1. In the first pass, we calculate the product of all elements to the left of each element.
2. In the second pass, we update each element with the product of all elements to the left of it multiplied by the product of all elements to the right of it.

This way, we effectively exclude the current element itself in the product calculation.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of elements in the array.
  - We perform two passes through the array, each taking linear time.
- Space Complexity: O(1) excluding the output array.
  - We use a single array `l` to store the product of all elements to the left of each element. No additional space is required.

## Summary

In this problem, we learned how to calculate the product of all elements in an array except for the current element efficiently without using division. By computing the product of prefixes and suffixes separately, we avoided division and achieved the desired linear time complexity.
