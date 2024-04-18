# String Compression

## Problem Statement

Given an array of characters `chars`, compress it using the following algorithm:

- Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
  - If the group length is greater than 1, append the character followed by the group length to `s`.
  - If the group length is 1, append the character to `s`.
- Modify the input array `chars` such that it contains the characters of `s`.

Return the length of the modified array after the compression.

## Approach 🌟

To solve this problem, we iterate through the array `chars` and maintain two pointers `i` and `j`. The pointer `i` is used to iterate through the array, while the pointer `j` is used to update the array in place.

1. Initialize pointers `i` and `j` to 0.
2. Iterate through the array `chars` using pointer `i`.
   - If the current character is the same as the next character, increment a counter `cur` and move to the next character.
   - If the current character is different from the next character, append the current character to the array at index `j`, and move pointer `j` accordingly.
     - If the counter `cur` is greater than 1, append the string representation of `cur` to the array at index `j`, and move pointer `j` accordingly.
   - Reset the counter `cur` to 1.
3. Update the array `chars` using pointer `j`.
4. Return the length of the updated array.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the length of the input array `chars`.
  - We iterate through the array once.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
