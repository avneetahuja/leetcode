# Max Vowels in a Substring of Given Length

## Problem Statement

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`. Vowel letters in English are (a, e, i, o, u).

## Approach 🌟

To find the maximum number of vowels in any substring of length `k` in the given string `s`, we can use a sliding window approach:

1. Initialize two pointers `l` and `r` to represent the left and right boundaries of the window, respectively. Also, initialize `count` and `max_count` to keep track of the number of vowels in the current window and the maximum number of vowels seen so far.
2. Slide the window to the right until the window size becomes equal to `k`.
   - While expanding the window, update `count` based on the vowels encountered.
3. Update `max_count` with the maximum of `max_count` and `count`.
4. Slide the window to the right by incrementing both `l` and `r`.
   - While sliding the window, update `count` to reflect the changes in the vowels included/excluded in the window.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the string `s`.
  - We traverse the string once using two pointers, each moving at most n steps.
- Space Complexity: O(1).
  - We use only a constant amount of extra space for storing variables.
