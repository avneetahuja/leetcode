# Longest Repeating Character Replacement 🔄

## Problem Statement

Given a string `s` that consists of only uppercase English letters, you can perform at most `k` operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest substring containing all repeating letters you can get after performing the above operations.

## Approach 🛠️

I've used a sliding window approach to find the length of the longest substring.

1. I initialized two pointers `i` and `j` to define a sliding window.
2. I created a dictionary `lCount` to store the count of characters in the current window.
3. I maintained a variable `mostFreq` to keep track of the most frequently occurring character in the current window.
4. I iterated through the string `s` using a while loop.
5. In each iteration:
   - I updated the count of characters in the current window based on the characters in `s`.
   - I updated the `mostFreq` variable to track the most frequently occurring character.
   - I adjusted the window by incrementing `i` until the number of characters not equal to the most frequent character is less than or equal to `k`.
   - I updated the answer with the maximum length of the current window.
   - I expanded the window by incrementing `j`.
6. The final result was the length of the longest substring.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The algorithm iterates through the string using a sliding window approach.
- Space Complexity: O(1), as the space used is independent of the size of the input string.
