# Combination Sum 💰🎯

## Problem Statement

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

Each number in `candidates` may only be used once in the combination.

## Approach 🌟

This problem can be solved using a backtracking approach. We can define a recursive function `f(i, s, li)` that generates all unique combinations starting from the `i`-th index with the current sum `s` and the list `li` representing the current combination.

### Steps:
1. Initialize an empty list `res` to store the unique combinations.
2. Define the recursive function `f(i, s, li)` that generates combinations.
   - If `i` reaches the length of `candidates`, return.
   - If the current sum `s` becomes negative, return.
   - If the current sum `s` becomes zero, append the current combination `li` to the result.
   - Recursively call `f(i, s - candidates[i], li + [candidates[i]])` to include the current element in the combination.
   - Recursively call `f(i + 1, s, li)` to exclude the current element from the combination.
3. Call the recursive function with the initial parameters `f(0, target, [])` to start the process.
4. Return the list of unique combinations.

## Complexity Analysis ⚙️

- Time Complexity: O(2^n)
  - The algorithm explores all possible combinations.
- Space Complexity: O(n)
  - The space required for storing the recursive call stack.
