# Valid Palindrome 🔄

## Problem Statement

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

**Example:**
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

## Approach 🛠️

I've used a two-pointer approach to check if the given string is a valid palindrome.

1. I initialized two pointers, `p1` and `p2`, pointing to the start and end of the string, respectively.
2. I converted the string to lowercase using `s.lower()` to ignore cases.
3. I used a while loop to iterate through the string.
4. In each iteration, I moved `p1` and `p2` towards the center of the string while skipping non-alphanumeric characters using `s[p1].isalnum()` and `s[p2].isalnum()`.
5. If the characters at `p1` and `p2` are not the same, the function returns `False`.
6. If the loop completes without finding any mismatch, the function returns `True`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The algorithm iterates through each character once.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
