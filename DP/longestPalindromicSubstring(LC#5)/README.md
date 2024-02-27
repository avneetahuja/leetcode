# Longest Palindromic Substring 🌐

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

## Approach 🛠️

The solution uses dynamic programming to find the longest palindromic substring. It maintains a 2D table `t` where `t[i][j]` represents the length of the palindromic substring ending at `s[i-1]` and `r[j-1]` (the reverse of `s`) if `s[i-1] == r[j-1]`, and 0 otherwise.

1. Initialize a 2D table `t` of size `(m+1) x (m+1)` where `m` is the length of the input string `s`.
2. Traverse the string using two nested loops (index `i` and index `j`).
3. If `s[i-1] == r[j-1]`, set `t[i][j] = 1 + t[i-1][j-1]`.
4. If `t[i][j]` is greater than the current maximum length (`maxx`), update `maxx`, `start`, and `end` accordingly.
5. If `s[i-1] != r[j-1]`, set `t[i][j] = 0` since no palindromic substring ends at these positions.
6. The result substring is given by `s[start:end]`.

## Complexity Analysis ⚙️

- Time Complexity: O(m^2), where m is the length of the input string.
  - The nested loops iterate over each character in the string, and the palindromic substring length is computed in constant time.
- Space Complexity: O(m^2), where m is the length of the input string.
  - The space used by the 2D table `t`.
