# Palindrome Partitioning 📝🔍

## Problem Statement

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

A palindrome string is a string that reads the same backward as forward.

## Approach 🚀

This problem can be solved using a backtracking approach. We can recursively partition the string into substrings and check if each substring is a palindrome. If a partitioned substring is a palindrome, we add it to the result.

### Steps:
1. Initialize an empty list `res` to store all possible palindrome partitions.
2. Define a recursive function `f(i, li)` that partitions the string starting from index `i` and appends the palindrome partitions to `li`.
3. In the `f` function:
   - If `i` reaches the end of the string (`len(s)`), append the current partition `li` to the result `res`.
   - Iterate over all possible indices `ind` starting from `i` to the end of the string.
   - Check if the substring from index `i` to `ind` is a palindrome. If it is, recursively call `f(ind+1, li + [sub])` to partition the remaining string.
4. Start the recursion from index `0` and an empty list `[]`.
5. Return the list `res` containing all possible palindrome partitions.

## Complexity Analysis ⚙️

- Time Complexity: O(2^N * N^2), where N is the length of the string `s`.
  - There can be 2^N possible partitioning combinations, and each partition's palindrome check takes O(N^2) time.
- Space Complexity: O(N * 2^N), where N is the length of the string `s`.
  - The space is used to store all possible partitioning combinations.
