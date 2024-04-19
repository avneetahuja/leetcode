# Can Place Flowers

## Problem Statement

You are given an integer array `flowerbed` representing the initial state of a garden. Each element in the array represents a plot where there may or may not be a flower planted.

You want to place `m` new flowers in this garden. The new flowers should not be planted directly next to existing flowers (i.e., they must be separated by at least one empty plot). You can assume the existence of an infinite number of empty plots at the beginning and end of the garden.

Determine if you can plant all the new flowers without violating the above rules.

## Approach 🌟

To solve this problem, we can iterate through the `flowerbed` array and count the number of available spaces where new flowers can be planted. We can then compare this count with the required number of new flowers `m` and return `True` if there are enough spaces.

1. Initialize a variable `count` to keep track of the number of available spaces for new flowers.
2. Iterate through the `flowerbed` array:
   - If the current plot and its adjacent plots are all empty, plant a flower at the current plot and increment the `count`.
3. After iterating through the array, check if the number of available spaces `count` is greater than or equal to the required number of new flowers `m`.
4. If the condition is satisfied, return `True`; otherwise, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the `flowerbed` array.
  - We iterate through the array once to count the available spaces.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
