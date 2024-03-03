# Maximum Profit with at Most K Transactions 📈

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most `k` transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Approach 📈

This problem can be solved using a dynamic programming approach. We can maintain a 2D array `dp`, where `dp[i][j]` represents the maximum profit on day `i` with `j` transactions.

### Steps:
1. Initialize two arrays, `after` and `cur`, each representing the maximum profit after the current day for each transaction count.
2. Iterate through the prices array from the last day to the first day.
   - For each day, iterate through the transaction counts (0 to `c`).
   - Update `cur[j][k]` based on whether a stock is bought or sold on the current day.
   - Update `after` with the values from `cur`.
3. Return the maximum profit from the first day with 1 transaction (`cur[1][0]`).

## Complexity Analysis ⚙️

- Time Complexity: O(c * n)
  - We iterate through the prices array for each transaction count.
- Space Complexity: O(c)
  - We use additional space to store the maximum profit for each transaction count.
