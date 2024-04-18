# Finding the Largest Altitude

## Problem Statement

Given an integer array `gain`, where `gain[i]` represents the net gain in altitude between points `i` and `i + 1` along a hiking trail, return the highest altitude among all the points.

## Approach 🌟

To solve this problem, we can simulate the hike along the trail and keep track of the current altitude. We'll initialize the current altitude to 0 and then update it as we move along the trail, taking into account the gain in altitude at each point.

1. Initialize a variable `highest` to store the highest altitude encountered so far.
2. Initialize a variable `current_altitude` to 0.
3. Iterate through the `gain` array:
   - Update the `current_altitude` by adding the gain at the current point.
   - Update the `highest` altitude if the `current_altitude` is greater than the `highest` altitude encountered so far.
4. Return the `highest` altitude.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the length of the `gain` array.
  - We iterate through the array once to calculate the altitudes.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
