# Koko Eating Bananas 🍌👩‍🍳

## Problem Statement

You have `n` piles of bananas where the `i`-th pile has `piles[i]` bananas. You have `h` hours to eat all the bananas.

Koko loves to eat bananas, and she eats with a speed of `k` bananas per hour. You can decide your `k` to minimize the total time it takes for Koko to eat all the bananas.

Given the integers `piles` and `h`, return the minimum integer `k` such that Koko can eat all the bananas within `h` hours.

## Approach 🛠️

I've implemented a binary search-based approach to find the minimum eating speed `k`.

1. I defined a helper function `getHours(piles, k)` that calculates the total time required to eat all the bananas at a given speed `k`.
2. I performed a binary search in the range `[1, max(piles)]` to find the minimum `k` such that Koko can eat all the bananas within `h` hours.

## Complexity Analysis ⚙️

- Time Complexity: O(n * log(max(piles))), where n is the number of piles.
  - The binary search is performed, and for each iteration, the `getHours` function is called.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
