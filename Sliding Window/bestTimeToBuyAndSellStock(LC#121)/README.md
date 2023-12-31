# Best Time to Buy and Sell Stock 📈💹

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Approach 🛠️

I've used a simple iterative approach to find the maximum profit.

1. I initialized two pointers `i` and `j` to represent the starting and ending days of a potential transaction.
2. I maintained a variable `maxD` to keep track of the maximum profit.
3. I used a variable `minSoFar` to track the minimum stock price encountered so far.
4. I iterated through the `prices` array using a while loop.
5. In each iteration:
   - If the current stock price is less than the minimum so far, I updated `minSoFar` and set `i` and `j` to the current index.
   - I calculated the potential profit (`prices[j] - prices[i]`) and updated `maxD` if the current profit is greater.
   - I expanded the window by incrementing `j`.
6. The final result was the maximum profit `maxD`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `prices`.
  - The algorithm iterates through the array once.
- Space Complexity: O(1), as the space used is independent of the size of the input array.
