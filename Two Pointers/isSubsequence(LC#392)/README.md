# Is Subsequence 🌐🔍

## Problem Statement

Given two strings `s` and `t`, return true if `s` is a subsequence of `t`. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Approach 🛠️

To determine if `s` is a subsequence of `t`, we can iterate through the characters of `t` and check if they match the characters of `s` in order.

1. Initialize a pointer `p` to 0.
2. Iterate through the characters of `t`.
   - If the current character of `t` is equal to the character at position `p` in `s`, increment `p`.
   - If `p` becomes equal to the length of `s`, return `True` (indicating that `s` is a subsequence of `t`).
3. If the loop completes without reaching the end of `s`, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(max(len(s), len(t)))
  - We iterate through the characters of both strings at most once.
- Space Complexity: O(1)
  - We use a constant amount of space.
