# Distinct Subsequences 🌐📜

## Problem Statement

Given two strings `x` and `y`, return the number of distinct subsequences of `x` that are equal to `y`. Since the result can be very large, return it modulo `10^9 + 7`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Approach 🛠️

We can solve this problem using dynamic programming. Let's define a 2D array `t` where `t[m][n]` represents the number of distinct subsequences of `x[:n+1]` that are equal to `y[:m+1]`.

We can formulate our approach using the following recurrence relation:

- If `x[n] == y[m]`, then `t[m][n] = t[m-1][n-1] + t[m][n-1]`.
  - This is because if the current characters match, we have two choices:
    1. Include the current character in the subsequence, which corresponds to `t[m-1][n-1]`.
    2. Exclude the current character, which corresponds to `t[m][n-1]`.
- If `x[n] != y[m]`, then `t[m][n] = t[m][n-1]`.
  - This is because if the current characters don't match, the only choice is to exclude the current character.

## Complexity Analysis ⚙️

- Time Complexity: O(len(x) * len(y))
  - We fill up the 2D array `t` of size len(y) * len(x).
- Space Complexity: O(len(x) * len(y))
  - We use a 2D array `t` for dynamic programming.
