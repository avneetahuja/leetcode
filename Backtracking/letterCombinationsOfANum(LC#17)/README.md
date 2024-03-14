# Letter Combinations of a Phone Number 📞🔤

## Problem Statement

Given a string `digits` containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Phone Keypad](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

## Approach 🚀

This problem can be solved using backtracking. We can recursively generate all possible combinations of letters for each digit in the input string.

### Steps:
1. Initialize a dictionary `keyboard` mapping each digit to its corresponding letters on the phone keypad.
2. Initialize an empty list `res` to store all possible letter combinations.
3. Define a recursive function `f(i, li)` that generates letter combinations starting from index `i` of the input string `digits`, where `li` is the current combination being formed.
4. In the `f` function:
   - If `i` reaches the end of the input string `digits`, append the current combination `li` to the result `res`.
   - Get the letters corresponding to the digit at index `i` from the `keyboard` dictionary.
   - Iterate over each letter and recursively call `f(i+1, li + c)` to form combinations with the next digit.
5. Start the recursion from index `0` and an empty string `""`.
6. Return the list `res` containing all possible letter combinations.

## Complexity Analysis ⚙️

- Time Complexity: O(3^N * 4^M), where N is the number of digits that map to 3 letters and M is the number of digits that map to 4 letters.
  - For digits that map to 3 letters, there are 3 possible letters, and for digits that map to 4 letters, there are 4 possible letters.
- Space Complexity: O(3^N * 4^M), where N is the number of digits that map to 3 letters and M is the number of digits that map to 4 letters.
  - The space is used to store all possible combinations.
