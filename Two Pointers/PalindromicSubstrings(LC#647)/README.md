# Count Palindromic Substrings 🌐

## Problem Statement

Given a string `s`, return the number of palindromic substrings in it.

A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

## Approach 🛠️

The solution counts palindromic substrings by iterating through each index of the string and treating it as the middle of a palindrome. There are two cases to consider:

1. Odd-length Palindromes:
   - Initialize pointers `l` and `r` to the current index.
   - Expand `l` and `r` outward while the characters at these positions are equal.
   - Count the palindromes found during expansion.

2. Even-length Palindromes:
   - Initialize pointers `l` to the current index and `r` to the next index.
   - Expand `l` and `r` outward while the characters at these positions are equal.
   - Count the palindromes found during expansion.

The total count is the sum of palindromes found in both cases.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2), where n is the length of the input string.
  - The nested loops iterate over each index in the string, and the expansion process is linear.
- Space Complexity: O(1)
  - Constant space is used.
