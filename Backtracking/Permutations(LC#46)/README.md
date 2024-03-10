# Permutations 🔄

## Problem Statement

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

## Approach 🌐

This problem can be solved using a backtracking approach to generate all possible permutations.

### Steps:
1. Initialize an empty list `res` to store the permutations.
2. Define the recursive function `f(i, li)` that generates permutations.
   - If the length of `li` is equal to the length of `nums`, append the current permutation `li` to the result.
   - Iterate over the elements of `nums`.
     - If the current element is not already present in `li`, recursively call `f(i + 1, li + [nums[ind]])` to include the current element in the permutation.
3. Call the recursive function with the initial parameters `f(0, [])` to start the process.
4. Return the list of permutations.

## Complexity Analysis ⚙️

- Time Complexity: O(n!)
  - The algorithm explores all possible permutations.
- Space Complexity: O(n)
  - The space required for storing the recursive call stack.
