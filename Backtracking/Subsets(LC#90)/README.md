# Subsets II 🔄✨

## Problem Statement

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

## Approach 🌐

This problem is an extension of finding all subsets, and we can use a backtracking approach with slight modifications to handle duplicates.

### Steps:
1. Initialize an empty list `res` to store the subsets.
2. Sort the input array `nums` to ensure that duplicate elements are adjacent.
3. Define the recursive function `f(i, li)` that generates subsets.
   - If `li` is not already present in `res`, append a copy of `li` to the result to avoid duplicates.
   - Iterate over the elements of `nums` starting from index `i`.
     - Recursively call `f(ind + 1, li + [nums[ind]])` to include the current element in the subset.
     - Skip duplicate elements to avoid duplicate subsets.
4. Call the recursive function with the initial parameters `f(0, [])` to start the process.
5. Return the list of subsets.

## Complexity Analysis ⚙️

- Time Complexity: O(2^n)
  - The algorithm explores all possible subsets.
- Space Complexity: O(n)
  - The space required for storing the recursive call stack.
