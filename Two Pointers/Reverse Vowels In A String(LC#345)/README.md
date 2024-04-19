# Reverse Vowels of a String

## Problem Statement

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u' in both uppercase and lowercase.

## Approach 🌟

To solve this problem, we can use a two-pointer approach:

1. Convert the input string `s` into a list of characters.
2. Initialize two pointers `l` and `r` to the start and end of the list, respectively.
3. Iterate through the list while `l` is less than `r`:
   - If `s[l]` is a vowel, move the pointer `r` towards the left until a vowel is found.
   - If `s[r]` is a vowel, move the pointer `l` towards the right until a vowel is found.
   - Swap `s[l]` and `s[r]`.
4. After the iteration, return the string formed by joining the characters of the modified list.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The two-pointer traversal takes O(n) time.
- Space Complexity: O(n).
  - We use extra space to convert the input string into a list of characters.
