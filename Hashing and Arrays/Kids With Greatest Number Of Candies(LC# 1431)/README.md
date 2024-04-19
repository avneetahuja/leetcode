# Kids With the Greatest Number of Candies

## Problem Statement

Given the array `candies` representing the number of candies that each kid has and an integer `extraCandies`, where `extraCandies` represents the number of extra candies that you have, determine if there is a way to distribute the extra candies such that each kid can have the greatest number of candies among them. A kid must have the greatest number of candies among all the kids to be considered having the greatest number of candies.

## Approach 🌟

To solve this problem, we need to find the maximum number of candies among all the kids in the array. Then, we iterate through the array and check if adding the extra candies to each kid's candies count will make them have the greatest number of candies. We store the result in a list and return it.

1. Initialize a list `res` of booleans, where each element represents whether the corresponding kid can have the greatest number of candies.
2. Find the maximum number of candies among all the kids in the array.
3. Iterate through the array `candies`:
   - If adding `extraCandies` to the current kid's candies count makes them have the greatest number of candies (i.e., greater than or equal to the maximum number of candies), set the corresponding element in `res` to `True`.
4. Return the list `res`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of kids (length of the `candies` array).
  - We iterate through the array once to find the maximum number of candies and once to check each kid's candies count.
- Space Complexity: O(n).
  - We use extra space to store the result list.
