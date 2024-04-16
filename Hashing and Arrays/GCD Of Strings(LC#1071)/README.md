# GCD of Strings

## Problem Statement

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`. 

Note that a string `x` divides string `y` if and only if `y` can be obtained by concatenating several copies of `x`.

## Approach 🌟

To find the largest string `x` that divides both `str1` and `str2`, we can use the following approach:
1. Iterate through all possible substrings of `str1` and `str2`, starting from the beginning.
2. For each substring `s` of `str1` and `str2`, if `s` divides both `str1` and `str2`, update the result `res` to `s`.
3. After finding the common substring `res`, check if it can be repeated to form `str1` and `str2` entirely.
4. If so, return `res`; otherwise, return an empty string.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2), where n is the length of the longer string between `str1` and `str2`.
  - We iterate through all possible substrings of `str1` and `str2`, resulting in a quadratic time complexity.
- Space Complexity: O(1)
  - We only use a constant amount of extra space.

## Summary

In this problem, we learned how to find the greatest common divisor (GCD) of two strings by iterating through all possible substrings. By checking if each substring divides both input strings and verifying if it can be repeated to form the input strings, we were able to find the desired result efficiently.
