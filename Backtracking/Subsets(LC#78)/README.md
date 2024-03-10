# Subsets 🧮

## Problem Statement

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets, and the subsets should be sorted in lexicographical order.

## Approach 🌟

This problem can be solved using a backtracking approach to generate all possible subsets.

### Steps:
1. Initialize an empty list `res` to store the subsets.
2. Define the recursive function `f(i, li)` that generates subsets.
   - Append the current subset `li` to the result.
   - Iterate over the elements of `nums` starting from index `i`.
     - Recursively call `f(ind + 1, li + [nums[ind]])` to include the current element in the subset.
3. Call the recursive function with the initial parameters `f(0, [])` to start the process.
4. Return the list of subsets.

## Complexity Analysis ⚙️

- Time Complexity: O(2^n)
  - The algorithm explores all possible subsets.
- Space Complexity: O(n)
  - The space required for storing the recursive call stack.
