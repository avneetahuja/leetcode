# Coin Change 🪙🔁

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Write a function to compute the minimum number of coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

## Approach 🛠️

The problem can be solved using dynamic programming. We will create a 2D array `t` where `t[i][j]` represents the minimum number of coins needed to make up amount `j` using the first `i` elements of the `coins` array.

1. Initialize the 2D array `t` with dimensions `(n + 1) x (amount + 1)`, where `n` is the length of the `coins` array.
2. Fill the array using dynamic programming:
   - For each coin denomination `coins[i]` and amount `j`:
     - If `coins[i]` is less than or equal to `j`, update `t[i][j]` using the minimum of:
       - 1 plus the minimum number of coins needed to make up the remaining amount (`t[i][j-coins[i]]`).
       - The minimum number of coins needed without using the current coin denomination (`t[i-1][j]`).
     - If `coins[i]` is greater than `j`, copy the value from the row above (`t[i-1][j]`).
3. The final answer is stored in `t[n][amount]`.

## Time Complexity

O(n * amount), where `n` is the length of the `coins` array.
