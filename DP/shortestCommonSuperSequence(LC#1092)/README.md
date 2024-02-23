# Shortest Common Supersequence 📜🔗

## Problem Statement

Given two strings `x` and `y`, find the shortest common supersequence (SCS). A supersequence is a string that contains both strings as subsequences.

## Approach and Time Complexity ⚙️

### Bottom-Up Dynamic Programming (DP)

To find the shortest common supersequence, we use bottom-up dynamic programming. We create a 2D table `t` to store the length of the longest common subsequence for substrings of `x` and `y`. We then trace back from the bottom-right corner of the table to reconstruct the shortest common supersequence string.

The time complexity of this approach is O(m * n), where m and n are the lengths of the input strings.
