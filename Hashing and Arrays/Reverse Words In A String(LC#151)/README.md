# Reverse Words in a String

## Problem Statement

Given a string `s`, reverse the order of characters in each word within the string while still preserving whitespace and initial word order.

## Approach 🌟

To reverse the order of words in the string, we can follow these steps:

1. Split the string `s` into a list of words using the `split()` function, which splits the string based on whitespace and returns a list of words.
2. Reverse the order of the words in the list using the `reverse()` function.
3. Join the reversed list of words into a single string using the `join()` function with whitespace as the separator.

Here's how the approach works:
- We split the string into words, reverse the order of words, and then join them back to form the reversed string.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - Splitting the string into words takes O(n) time.
  - Reversing the list of words takes O(n) time.
  - Joining the words back into a string takes O(n) time.
- Space Complexity: O(n), where n is the length of the input string `s` (for storing the list of words).

## Summary

In this problem, we learned how to reverse the order of words in a string while preserving whitespace and initial word order. By splitting the string into words, reversing the order of words, and then joining them back, we achieved the desired result.
