# Group Anagrams 🤝

## Problem Statement

Given an array of strings `strs`, group the anagrams together. An Anagram is a word or phrase formed by rearranging the letters of another.

Return a list of the groups of anagrams.

**Example:**
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

## Approach 🛠️

I've used a Python class-based solution that utilizes a dictionary to group anagrams based on their character counts.

1. I initialized a `defaultdict` called `map` with lists as default values.
2. I iterated through each string `s` in the input array `strs`.
3. For each string `s`, I created a count of characters using a list `count`, where `count[i]` represents the count of the `i`-th character ('a' to 'z') in the string.
4. I converted the count list to a tuple and used it as the key in the `map` dictionary.
5. I appended the current string `s` to the list associated with the computed key in the `map`.
6. The function returned the values (groups of anagrams) from the `map`.

## Complexity Analysis ⚙️

- Time Complexity: O(N * K), where N is the length of the input array `strs` and K is the average length of strings in `strs`.
  - The outer loop iterates through each string in `strs`.
  - The inner loop iterates through each character in a string.
- Space Complexity: O(N * K), where N is the length of the input array `strs` and K is the average length of strings in `strs`.
  - The space used by the `map` dictionary.
