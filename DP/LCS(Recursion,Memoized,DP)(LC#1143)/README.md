# Longest Common Subsequence 📜🔄

## Problem Statement

Given two strings `text1` and `text2`, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

## Approaches and Time Complexities ⚙️

### Recursive Solution

The naive approach involves using recursion to explore all possible common subsequences. This approach has an exponential time complexity and is not efficient for larger inputs.

### Memoized Version

To optimize the recursive solution, we can use memoization. We create a memoization table `t` to store the results of subproblems. This reduces the time complexity to O(m * n), where m and n are the lengths of the input strings.

### Bottom-Up Dynamic Programming (DP)

The most efficient approach involves using bottom-up dynamic programming. We create a 2D table `t` and fill it in a bottom-up manner. This approach also has a time complexity of O(m * n) and avoids the function call overhead of recursion.
