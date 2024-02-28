# House Robber 🏠💰

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Approach 🛠️

Dynamic Programming can be used to solve this problem. We maintain an array `v` where `v[i]` represents the maximum amount of money that can be robbed from the first `i` houses. The recurrence relation is given by:

`v[i] = max(nums[i-1] + v[i-2], v[i-1])`


The base cases are `v[1] = nums[0]` and `v[2] = max(nums[0], nums[1])`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of houses.
  - The algorithm iterates over all houses once.
- Space Complexity: O(n)
  - Additional space is used to store the dynamic programming array.
