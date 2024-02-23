# Longest Common Substring 📜🔗

## Problem Statement

Given two strings `x` and `y`, find the length of the longest common substring.

A substring is a contiguous sequence of characters within a string. A common substring is a substring that is common to both strings.

## Approach and Time Complexity ⚙️

### Bottom-Up Dynamic Programming (DP)

To find the length of the longest common substring, we can use bottom-up dynamic programming. We create a 2D table `t` and fill it in a bottom-up manner. The value `t[i][j]` represents the length of the common substring ending at `x[i-1]` and `y[j-1]`.

The maximum value in the table will be the length of the longest common substring. We use a variable `maxx` to keep track of the maximum length during the process.

The time complexity of this approach is O(m * n), where m and n are the lengths of the input strings.
