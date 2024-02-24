# Longest Repeating Subsequence 📏

## Problem Statement

Given a string `st`, find the length of the longest repeating subsequence (LRS). A repeating subsequence is a subsequence that appears at least twice in the original string without overlapping.

## Approach and Time Complexity ⚙️

### Dynamic Programming

To find the length of the longest repeating subsequence, we can use dynamic programming. Let's define a 2D table `t` where `t[i][j]` represents the length of the longest repeating subsequence in the substring `st[i-1:j-1]`.

- Initialize the table `t` with zeros.
- Traverse the string and fill the table based on the characters:
  - If `st[i-1]` is equal to `st[j-1]` and `i` is not equal to `j`, update `t[i][j] = 1 + t[i-1][j-1]`.
  - Otherwise, update `t[i][j]` by taking the maximum of `t[i-1][j]` and `t[i][j-1]`.

The length of the longest repeating subsequence will be the value in the bottom-right corner of the table, i.e., `t[m][m]`, where `m` is the length of the input string.

The time complexity of this approach is O(m^2), where `m` is the length of the input string.
