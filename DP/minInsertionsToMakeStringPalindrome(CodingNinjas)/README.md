# Minimum Insertions to Make a String Palindrome 📉

## Problem Statement

Given a string `str`, find the minimum number of insertions needed to make it a palindrome.

## Approach and Time Complexity ⚙️

### Dynamic Programming

To find the minimum insertions, we can use dynamic programming. Let's define a 2D table `t` where `t[i][j]` represents the length of the longest palindromic subsequence in the substring `str[i-1:j-1]`.

- Initialize the table `t` with zeros.
- Traverse the string from both ends and fill the table based on the characters:
  - If `str[i-1]` is equal to `s[j-1]` (where `s` is the reverse of `str`), update `t[i][j] = 1 + t[i-1][j-1]`.
  - Otherwise, update `t[i][j]` by taking the maximum of `t[i-1][j]` and `t[i][j-1]`.

The minimum insertions needed will be the difference between the length of the input string and the length of the longest palindromic subsequence, i.e., `m - t[m][m]`, where `m` is the length of the input string.

The time complexity of this approach is O(m^2), where `m` is the length of the input string.
