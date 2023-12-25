# Encode and Decode Strings 🔄

## Problem Statement

You are given two methods to encode and decode strings. The `encode` method takes a list of strings and converts them into a single string, and the `decode` method takes a string and converts it back into a list of strings.

**Example:**
- Input: ["string1", "string2", "string3"]
  Output: "string1:;string2:;string3"

## Approach 🛠️

I've used a Python class-based solution for encoding and decoding strings.

### `encode` 🚀

1. I initialized an empty string called `res` to concatenate the encoded strings.
2. I iterated through the list of strings `strs`.
3. For each string `s` in `strs`, I appended `s + ":;"` to the result string.
4. The final result string is returned after removing the last ":;" to maintain the correct format.

### `decode` 📚

1. I split the input string `s` using the ":;" delimiter, creating a list of strings.
2. The list of strings is returned as the decoded result.

## Complexity Analysis ⚙️
### Encode Method:

Time Complexity: O(N), where N is the total length of all strings in the input list strs.
The method iterates through each string in the list.
Space Complexity: O(N), where N is the total length of all strings in the input list strs.
The method creates a single encoded string.

### Decode Method:

Time Complexity: O(N), where N is the length of the input string s.
The method splits the input string based on the delimiter.
Space Complexity: O(N), where N is the length of the input string s.
The method creates a list of strings during the split operation.
