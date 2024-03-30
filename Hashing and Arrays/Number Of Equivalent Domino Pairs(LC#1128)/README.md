# Equivalent Domino Pairs 🎲

## Problem Statement

You are given a list of dominoes where each domino is represented by a pair of integers `[a, b]`. Two dominoes `dominoes[i]` and `dominoes[j]` are considered equivalent if they have the same values, disregarding the order.

Design an algorithm to find the number of pairs `(i, j)` such that `i < j` and `dominoes[i]` is equivalent to `dominoes[j]`.

## Approach 🎲

To solve this problem, we can use a dictionary to count the occurrences of each pair of integers in the dominoes. Since we want to disregard the order of integers in each domino, we can sort each domino pair before counting. After counting the occurrences, we iterate through the dictionary and calculate the number of equivalent pairs using the combination formula.

### Steps:
1. Initialize an empty dictionary `seen` to store the counts of equivalent domino pairs.
2. Iterate through each domino in the list:
   - Sort the domino pair to ensure consistent representation.
   - Update the count in the `seen` dictionary for the sorted pair.
3. Initialize a variable `count` to store the total number of equivalent pairs.
4. Iterate through the `seen` dictionary:
   - For each key-value pair:
     - If the count is greater than 1, calculate the number of equivalent pairs using the combination formula `math.comb(value, 2)`.
     - Add the calculated value to the `count`.
5. Return the `count`.

## Complexity Analysis ⚙️

- Time Complexity: O(N)
  - We iterate through the list of dominoes once to count the occurrences.
- Space Complexity: O(N)
  - We use a dictionary to store the counts of domino pairs, which can have up to N entries.
