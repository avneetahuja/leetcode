# Best Time to Buy and Sell Stock III 📈📈

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Approach 📈

This problem can be solved using a dynamic programming approach. We can define a function `f(i, b, c)` that represents the maximum profit that can be achieved by day `i` with the option to buy or sell (`b` is 1 for buy, 0 for sell) and the count of transactions made so far (`c`).

### Steps:
1. Initialize a 3D array `t` to store the results of subproblems. Set all entries to -1 to indicate that the result is not yet calculated.
2. Define the recursive function `f(i, b, c)` that calculates the maximum profit by considering the options to buy or sell on day `i` and the count of transactions.
   - If `b` is 1 (allowed to buy), update `t[i][b][c]` by taking the maximum of either buying on day `i` and proceeding to the next day without buying or skipping the purchase on day `i` and moving to the next day with the option to buy.
   - If `b` is 0 (allowed to sell), update `t[i][b][c]` by taking the maximum of either selling on day `i` and proceeding to the next day with the option to buy or skipping the sale on day `i` and moving to the next day without buying.
3. Call the recursive function with the initial parameters `f(0, 1, 0)` to start the process from the first day with the option to buy and no transactions made.
4. Return the result.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - The recursive function is called once for each day, and the results are memoized in the 3D array.
- Space Complexity: O(n)
  - We use additional space for memoization in the 3D array.
