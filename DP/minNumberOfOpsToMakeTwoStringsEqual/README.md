# Minimum Number of Operations to Make Two Strings Equal 📜✂️🔗

## Problem Statement

Given two strings `x` and `y`, find the minimum number of operations required to make them equal. The allowed operations are insertion, deletion, or substitution of a character.

## Approach and Time Complexity ⚙️

### Longest Common Subsequence (LCS) based

The minimum number of operations to make two strings equal is related to the length of their LCS. We can find the length of the LCS using bottom-up dynamic programming. Once we have the LCS length, we can calculate the minimum number of operations using the formula:

\[ \text{min_operations} = \text{length of } x + \text{length of } y - 2 \times \text{length of LCS} \]

The time complexity of this approach is O(m * n), where m and n are the lengths of the input strings.
