# Permutation in String 🔄🔍

## Problem Statement

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

In other words, return `True` if one of the permutations of `s1` is a substring of `s2`.

## Approach 🛠️

I've used a sliding window approach to check for the presence of a permutation of `s1` in `s2`.

1. I created a dictionary `lCount` to store the count of characters in string `s1`.
2. I initialized variables `k` and `count` representing the length of `s1` and the count of distinct characters in the current window, respectively.
3. I used two pointers `i` and `j` to define a sliding window in `s2`.
4. I iterated through `s2` using a while loop.
5. In each iteration:
   - I updated the count of characters in the current window based on the characters in `s1`.
   - If the count becomes zero, it means a permutation of `s1` is found in the current window, and I returned `True`.
   - I adjusted the window by incrementing `i`.
   - I expanded the window by incrementing `j`.
6. If the loop completes without finding a permutation, I returned `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s2`.
  - The algorithm iterates through the string using a sliding window approach.
- Space Complexity: O(m), where m is the size of the character set in `s1`.
  - The space used by the `lCount` dictionary is proportional to the size of the character set.
