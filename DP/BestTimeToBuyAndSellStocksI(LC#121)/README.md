# Best Time to Buy and Sell Stock 💹

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

Return the maximum profit you can achieve from buying one stock on day `i` and selling it on day `j` where `i <= j`.

If you cannot achieve any profit, return `0`.

## Approach 📈

We can solve this problem with a simple one-pass approach. The idea is to keep track of the minimum price (`minSoFar`) while iterating through the array. For each day, we calculate the profit by subtracting the minimum price encountered so far from the current day's price. If this profit is greater than the maximum profit (`maxx`), we update `maxx`. This way, we find the maximum profit achievable by buying and selling the stock.

### Steps:
1. Initialize `maxx` to 0 and `minSoFar` to the price on the first day (`prices[0]`).
2. Iterate through the prices starting from the second day (`i = 1`).
    - Update `minSoFar` by taking the minimum of the current price and `minSoFar`.
    - Update `maxx` by taking the maximum of the difference between the current price and `minSoFar` and `maxx`.
3. Return `maxx` as the result.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - We iterate through the prices array once.
- Space Complexity: O(1)
  - We use constant space to store `maxx` and `minSoFar`.
