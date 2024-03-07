# Maximum Product Subarray 🌐✖️

## Problem Statement

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) that has the largest product.

Return the maximum product.

## Approach 🌟

This problem can be solved using a simple iterative approach by maintaining two variables, `pre` and `suf`, to keep track of the prefix and suffix products while iterating through the array.

### Steps:
1. Initialize variables `pre`, `suf`, and `maxx` to 1 and set `maxx` to a very small value to store the maximum product.
2. Iterate through the array.
   - If `pre` becomes 0, set it back to 1 to handle zero values.
   - If `suf` becomes 0, set it back to 1 to handle zero values.
   - Update `pre` and `suf` by multiplying with the current element in the array.
   - Update `maxx` with the maximum of `pre`, `suf`, and the current maximum.
3. Return the maximum product stored in `maxx`.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - The algorithm iterates through the array once.
- Space Complexity: O(1)
  - Constant space is used.
