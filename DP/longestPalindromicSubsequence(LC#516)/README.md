# Longest Palindromic Subsequence 📜🔄

## Problem Statement

Given a string `s`, find the length of the longest palindromic subsequence in it.

## Approach and Time Complexity ⚙️

### Dynamic Programming

To find the longest palindromic subsequence, we can use dynamic programming. Let's define a 2D table `t` where `t[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i-1:j-1]`.

- Initialize the table `t` with zeros.
- Traverse the string from both ends and fill the table based on the characters:
  - If `s[i-1]` is equal to `s2[j-1]` (where `s2` is the reverse of `s`), update `t[i][j] = 1 + t[i-1][j-1]`.
  - Otherwise, update `t[i][j]` by taking the maximum of `t[i-1][j]` and `t[i][j-1]`.

The length of the longest palindromic subsequence will be stored in `t[m][m]`, where `m` is the length of the input string.

The time complexity of this approach is O(m^2), where m is the length of the input string.
