# Merge Strings Alternately

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the remaining letters of the longer string to the merged string.

Return the merged string.

## Approach 🌟

To merge the strings alternately, we can use two pointers to iterate through `word1` and `word2`. We'll keep appending characters from both strings alternately until we reach the end of one of the strings. Then, we'll append the remaining characters of the longer string to the merged string.

Here's how the approach works:
1. Initialize two pointers `p1` and `p2` to 0 and an empty string `res` to store the merged string.
2. Find the minimum length of `word1` and `word2` (`limit`).
3. While `p1` is less than `limit`, append `word1[p1]` and `word2[p1]` to `res` alternately and increment `p1`.
4. If `word1` is longer than `word2`, append the remaining characters of `word1` starting from index `p1` to `res`.
5. If `word2` is longer than `word1`, append the remaining characters of `word2` starting from index `p1` to `res`.
6. Return the merged string `res`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the longer string between `word1` and `word2`.
- Space Complexity: O(n), where n is the length of the merged string.
