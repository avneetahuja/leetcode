# Repeated DNA Sequences 🧬🔁

## Problem Statement

The problem is to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

## Approach 🌟

This problem can be solved efficiently using a sliding window approach. We can maintain a sliding window of length 10 and use a dictionary (`map`) to keep track of the frequency of each 10-letter sequence.

### Steps:
1. Initialize an empty dictionary `map` to store the frequency of each 10-letter sequence.
2. Initialize an empty list `res` to store the repeated DNA sequences.
3. Iterate through the given DNA sequence using a sliding window of length 10.
   - Update the frequency of the current 10-letter sequence in the dictionary `map`.
   - If the frequency becomes 2, append the sequence to the `res` list.
4. Return the list of repeated DNA sequences.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - The algorithm iterates through the given DNA sequence once.
- Space Complexity: O(n)
  - The dictionary `map` is used to store the frequency of 10-letter sequences.
