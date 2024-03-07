# Min Cost Climbing Stairs ⬆️💰

## Problem Statement

You are given an array `cost` where `cost[i]` is the cost of climbing the `i`-th stair. Each time you can either climb one or two steps. Return the minimum cost to reach the top of the floor.

You can start from the step with index 0 or 1.

## Approach 🚶‍♂️

This problem can be solved using a dynamic programming approach. We can define a function `f(i)` that represents the minimum cost to reach the `i`-th stair.

### Steps:
1. Initialize an array `v` to store the results of subproblems. Set all entries to -1 to indicate that the result is not yet calculated.
2. Define the recursive function `f(i)` that calculates the minimum cost by considering the options to climb either one or two steps.
   - If `i` is 0 or 1, return `cost[i]`.
   - If `v[i]` is not -1, return `v[i]`.
   - Otherwise, update `v[i]` by taking the minimum of either climbing one step from the previous stair or climbing two steps from the stair before that, plus the cost of the current stair.
3. Call the recursive function with the initial parameter `f(len(cost)-1)` to start the process from the last stair.
4. Return the result.

## Complexity Analysis ⚙️

- Time Complexity: O(n)
  - The recursive function is called once for each stair, and the results are memoized in the array.
- Space Complexity: O(n)
  - We use additional space for memoization in the array.
