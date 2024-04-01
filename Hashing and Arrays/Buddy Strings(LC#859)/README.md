# Buddy Strings 🤝

## Problem Statement

You are given two strings `s` and `goal`. Determine if swapping any two characters in `s` results in a string that is equal to `goal`. Return `true` if the swapping is possible; otherwise, return `false`.

To be able to swap two characters in `s`, the following conditions must be met:
1. The length of `s` and `goal` must be the same.
2. There should be exactly two characters in `s` that are different from `goal`.
3. If there are more than two characters different, at least one character must be repeated in `s`.

## Approach 🤝

To solve this problem, we can follow these steps:
1. Check if the sorted versions of strings `s` and `goal` are equal. If they are not, return `False` because no swapping can make them equal.
2. Initialize an empty string `res` to store characters in `s` that are different from `goal`.
3. Initialize a dictionary `seen` to keep track of the count of characters in `s`.
4. Iterate through each character in `s` and update the count of characters in the `seen` dictionary.
5. Keep track of the maximum count of any character (`maxC`) in `s`.
6. If the length of `res` is exactly 2, return `True` because only two characters need to be swapped to make `s` equal to `goal`.
7. If `maxC` is greater than 1 and the length of `res` is less than 3, return `True` because there are more than two characters different in `s`, but at least one character is repeated, so swapping can make `s` equal to `goal`.
8. If none of the above conditions are met, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - Sorting the strings takes O(nlogn) time, where n is the length of the strings. The subsequent iterations take O(n) time.
- Space Complexity: O(n)
  - We use extra space for storing characters in `res` and the `seen` dictionary.
