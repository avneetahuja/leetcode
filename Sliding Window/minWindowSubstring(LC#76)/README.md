# Minimum Window Substring 🪟

## Problem Statement

Given a string `s` and a string `t`, find the minimum window in `s` which will contain all the characters in `t` in complexity O(n).

If there is no such window in `s` that covers all characters in `t`, return an empty string `""`.

## Approach 🛠️

I've used a sliding window approach to find the minimum window substring.

1. I created a dictionary `lcount` to store the count of characters in string `t`.
2. I initialized a variable `count` to keep track of the number of characters remaining to be matched.
3. I used two pointers `i` and `j` to define a sliding window.
4. I iterated through the string `s` using a while loop.
5. In each iteration:
   - I updated the count of characters in the current window based on the characters in `t`.
   - If the count becomes zero, it means all characters in `t` are present in the current window.
   - I updated the minimum window substring (`mn`) if the current window is smaller than the previous minimum or if it's the first valid window.
   - I adjusted the window by incrementing `i` until it becomes invalid again (count becomes non-zero).
6. The final result was the minimum window substring.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The algorithm iterates through the string using a sliding window approach.
- Space Complexity: O(m), where m is the size of the character set in string `t`.
  - The space used by the `lcount` dictionary is proportional to the size of the character set.
