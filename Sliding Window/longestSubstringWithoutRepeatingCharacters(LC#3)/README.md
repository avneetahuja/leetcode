# Longest Substring Without Repeating Characters 📏

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

## Approach 🛠️

I've used a sliding window approach to find the length of the longest substring without repeating characters.

1. I initialized pointers `i` and `j` to define a sliding window.
2. I used a while loop to iterate through the string `s`.
3. In each iteration:
   - I updated the count of characters in the current window (`lcount` dictionary).
   - If the length of the unique characters in the window is equal to the size of the window, I updated the maximum length (`mx`).
   - If the length of unique characters is less than the size of the window, I adjusted the window by incrementing `i` until it became valid again.
4. The final result was the maximum length of a substring without repeating characters.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The algorithm iterates through the string using a sliding window approach.
- Space Complexity: O(min(n, m)), where n is the length of the input string `s` and m is the size of the character set (number of distinct characters).
  - The space used by the `lcount` dictionary is proportional to the size of the character set.
