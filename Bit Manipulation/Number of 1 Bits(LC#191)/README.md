# Number of 1 Bits 🧮

## Problem Statement

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## Approach 🚀

To count the number of '1' bits in an unsigned integer:
1. Convert the integer to its binary representation.
2. Count the number of '1' characters in the binary string representation.

### Steps:
1. Convert the integer `n` to its binary representation using the `bin()` function.
2. Convert the binary representation to a string.
3. Use the `count()` method to count the number of '1' characters in the string.

## Complexity Analysis ⚙️

- Time Complexity: O(log n)
  - The time complexity is determined by the number of bits in the binary representation of the integer `n`.
- Space Complexity: O(1)
  - We use constant space for variables.
