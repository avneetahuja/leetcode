# Remove Stars from a String

## Problem Statement
Given a string `s` containing characters and '*' symbols, remove all the stars and the character immediately preceding each star. Return the resulting string.

## Approach

### Steps

1. **Use a Stack**:
   - Use a stack to help with the removal of characters.
   - Iterate through each character in the string.
   - If the character is '*', pop the top element from the stack (this simulates removing the preceding character).
   - If the character is not '*', push it onto the stack.

2. **Construct the Result**:
   - After processing all characters, the stack will contain the resulting characters in order.
   - Join the characters in the stack to form the final string.

### Solution Code

```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
```

### Explanation

1. **Using a Stack**:
   - Initialize an empty stack.
   - Iterate through the string:
     - If the current character is '*', remove the top character from the stack.
     - Otherwise, add the current character to the stack.

2. **Constructing the Result**:
   - After the iteration, the stack contains the characters of the resulting string in the correct order.
   - Convert the stack into a string by joining its elements.

### Time Complexity
- The time complexity of this solution is O(n), where n is the length of the string. This is because each character is processed once.

### Space Complexity
- The space complexity is O(n) in the worst case, which occurs when the string contains no '*' characters and all characters are added to the stack.
