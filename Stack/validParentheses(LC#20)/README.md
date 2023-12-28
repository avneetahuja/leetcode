# Valid Parentheses ✅

## Problem Statement

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

**Example:**
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

## Approach 🛠️

I've used a stack-based approach to check the validity of the input string.

1. I initialized an empty list `stack` to simulate a stack data structure.
2. I iterated through each character `c` in the input string `s`.
3. If `c` is an open bracket ('(', '{', '['), I pushed it onto the stack.
4. If `c` is a closing bracket (')', '}', ']'), I checked if the stack is empty or if the corresponding open bracket is at the top of the stack.
5. If the conditions in step 4 are not met, the string is not valid, and I returned `False`.
6. If the loop completes and the stack is empty, the string is valid, and I returned `True`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input string `s`.
  - The algorithm iterates through each character once.
- Space Complexity: O(n), where n is the length of the input string `s`.
  - The space used by the stack is proportional to the number of open brackets.
