# Find All Anagrams in a String 🧩

## Problem Statement

Given a string `s` and a non-empty string `p`, find all the start indices of `p`'s anagrams in `s`.

Strings consist of lowercase English letters only.

## Approach 🛠️

I've used a sliding window approach to find all the start indices of anagrams of `p` in the main string `s`.

1. I initialized a dictionary `lcount` to store the count of each character in the string `p`.
2. I iterated through the characters of `p` and populated the `lcount` dictionary.
3. I initialized a variable `count` to store the distinct letter count in `p`.
4. I initialized pointers `i` and `j` to define a sliding window of size `k` (length of `p`).
5. I used a while loop to iterate through the main string `s`.
6. In each iteration, I updated the `lcount` dictionary based on the characters in the sliding window.
7. If the size of the sliding window is less than `k`, I expanded the window by incrementing `j`.
8. If the size of the sliding window is equal to `k`, I checked if the count of distinct letters in the window is zero.
9. If the count is zero, an anagram is found, and I appended the start index `i` to the result list.
10. I moved the sliding window by incrementing `j` and `i`.
11. The loop continued until `j` reached the end of the main string.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the main string `s`.
  - The algorithm iterates through the main string using a sliding window approach.
- Space Complexity: O(k), where k is the length of the string `p`.
  - The algorithm uses a dictionary to store the count of characters in the string `p`.
