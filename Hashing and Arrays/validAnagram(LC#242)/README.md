# Valid Anagram ✨

## Problem Statement

Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`.

An Anagram is a word or phrase formed by rearranging the letters of another.

**Example:**
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False

## Approach 🛠️

I've used a Python class-based solution by checking if the sorted representation of both strings is equal.

1. I used the `sorted` function to obtain a sorted list of characters for each string `s` and `t`.
2. I compared the sorted lists to check if they are equal.
3. If the sorted representations are equal, the strings are anagrams, and the function returns `True`.
4. Otherwise, it returns `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(n log n), where n is the length of the longer of the two strings `s` and `t`.
  - Sorting the strings takes O(n log n) time.
- Space Complexity: O(n), where n is the length of the longer of the two strings `s` and `t`.
  - The space used for the sorted representation.
