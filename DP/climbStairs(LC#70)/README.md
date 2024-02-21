# Climbing Stairs 🧗‍♂️

## Problem Statement

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Return the number of ways to reach the top.

## Approach 🛠️

To efficiently calculate the number of ways to climb to the top, we can use a space-optimized approach. We only need to store the last two counts of ways to reach the current step. We can initialize two variables `prev2` and `prev` to `2` and `3` respectively (as there are 2 ways to climb 1 step and 3 ways to climb 2 steps). Then, iterate from `4` to `n` and calculate the next count using the formula `ways(n) = ways(n-1) + ways(n-2)`. Update `prev2` and `prev` accordingly.

## Complexity Analysis ⚙️

The time complexity for this approach is O(n), and the space complexity is O(1).
