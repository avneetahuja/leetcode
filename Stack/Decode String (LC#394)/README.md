# Decode String

## Problem Description

Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

## Approach

### Steps

1. **Initialize a Stack**:
   - Use a stack to help keep track of characters and numbers during decoding.
   
2. **Iterate Through the String**:
   - For each character in the string:
     - If the character is `']'`, it signifies the end of an encoded segment.
       - Pop characters from the stack until encountering `'['`, and reverse them to form the `string_to_append`.
       - Discard the `'['` from the stack.
       - Then, collect the digits representing the number `k` and convert them to an integer.
       - Append the `string_to_append` to the stack `k` times.
     - If the character is not `']'`, simply append it to the stack.

3. **Return the Decoded String**:
   - After processing all characters, join the stack to form the decoded string.

### Solution Code

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                string_to_append = ""
                while stack[-1] != '[':
                    string_to_append += stack.pop()
                stack.pop()
                num_string = ""
                while stack and stack[-1].isdigit():
                    num_string = stack.pop() + num_string
                for k in range(int(num_string)):
                    for j in range(len(string_to_append)-1, -1, -1):
                        stack.append(string_to_append[j])
            else:
                stack.append(c)
        return ''.join(stack)
```


### Time Complexity
- The time complexity of this solution is O(n), where n is the length of the input string `s`. This is because each character is processed at most twice (once when pushing to the stack and once when popping from it).

### Space Complexity
- The space complexity is O(n) in the worst case, where all characters are stored in the stack.
