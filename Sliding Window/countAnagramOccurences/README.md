# Count Substring Anagrams 🧩

## Problem Statement

Given a string `str` and a substring `sub`, count the number of anagrams of the substring that appear as contiguous substrings in the main string.

**Example:**
Input: str = "cbaebabacd", sub = "abc"
Output: 2
Explanation: The anagrams "cba" and "bca" appear as contiguous substrings in the main string.

## Approach 🛠️

I've used a sliding window approach to count the number of anagrams of the substring `sub` in the main string `str`.

1. I initialized a dictionary `lcount` to store the count of each character in the substring `sub`.
2. I iterated through the characters of `sub` and populated the `lcount` dictionary.
3. I initialized a variable `count` to store the distinct letter count in `sub`.
4. I initialized pointers `i` and `j` to define a sliding window of size `k` (length of `sub`).
5. I used a while loop to iterate through the main string.
6. In each iteration, I updated the `lcount` dictionary based on the characters in the sliding window.
7. If the size of the sliding window is less than `k`, I expanded the window by incrementing `j`.
8. If the size of the sliding window is equal to `k`, I checked if the count of distinct letters in the window is zero.
9. If the count is zero, an anagram is found, and I incremented the `anagramCount`.
10. I moved the sliding window by incrementing `j` and `i`.
11. The loop continued until `j` reached the end of the main string.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the main string `str`.
  - The algorithm iterates through the main string using a sliding window approach.
- Space Complexity: O(k), where k is the length of the substring `sub`.
  - The algorithm uses a dictionary to store the count of characters in the substring.
