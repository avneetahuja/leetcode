# Read N Characters Given Read4

## Problem Statement

You have a function `read4` which reads 4 characters at a time from a file. The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file. By using the `read4` function, implement the function `read` that reads `n` characters from the file and store it in the buffer array `buf`. Consider that you cannot manipulate the file directly and that the `read4` function may be called multiple times.

## Approach 🌟

To read `n` characters from the file using the `read4` function, we can follow these steps:

1. If `n` is less than or equal to 4, simply call `read4` and copy the characters into `buf`. If there are extra spaces in `buf`, remove them and return `n`.
2. If `n` is greater than 4, calculate the quotient and remainder when dividing `n` by 4. We'll need to call `read4` for each group of 4 characters, as well as one additional call for the remainder.
3. Iterate `quotient + 1` times, calling `read4` each time and copying the characters into `buf`.
4. After copying the characters, remove any extra spaces in `buf` if `n` is not a multiple of 4 (i.e., there's a remainder).
5. Return `n` if it's less than the length of `buf`; otherwise, return the length of `buf`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of characters to read. We may need to call `read4` multiple times, but each call reads at most 4 characters.
- Space Complexity: O(1). We're only using a constant amount of space for variables and the buffer array `buf`.

Feel free to reach out again if you have any more questions.
