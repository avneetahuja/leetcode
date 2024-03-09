# Combination Sum II 💰🎯

## Problem Statement

Given a collection of candidate numbers `candidates` and a target number `target`, find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination, and the solution set must not contain duplicate combinations.

## Approach 🌟

This problem can be solved using a backtracking approach with a slight modification to handle duplicate elements. We can sort the `candidates` array to easily skip duplicates during the exploration process.

### Steps:
1. Sort the `candidates` array to handle duplicates easily.
2. Initialize an empty list `res` to store the unique combinations.
3. Define the recursive function `f(li, i, s)` that generates combinations.
   - If the current sum `s` becomes zero, append the current combination `li` to the result.
   - If the current sum `s` becomes negative, return.
   - Iterate over the `candidates` starting from index `i`.
     - Skip duplicate elements to avoid redundant combinations.
     - Recursively call `f(li + [candidates[ind]], ind + 1, s - candidates[ind])` to include the current element in the combination.
4. Call the recursive function with the initial parameters `f([], 0, target)` to start the process.
5. Return the list of unique combinations.

## Complexity Analysis ⚙️

- Time Complexity: O(2^n)
  - The algorithm explores all possible combinations.
- Space Complexity: O(n)
  - The space required for storing the recursive call stack.
