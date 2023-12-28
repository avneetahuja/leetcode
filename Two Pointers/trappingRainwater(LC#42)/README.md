# Trapping Rain Water 🪤🌧️

## Problem Statement

Given an array of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example:**
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map traps 6 units of rainwater.

## Approach 🛠️

I've used a two-pointer approach to calculate the amount of trapped rainwater in the elevation map.

1. I initialized two pointers `p1` and `p2` at the beginning and end of the elevation map, respectively.
2. I initialized variables `lmax` and `rmax` to keep track of the maximum height encountered from the left and right, respectively.
3. I initialized a variable `totalWater` to store the total trapped rainwater.
4. I used a while loop to iterate through the elevation map.
5. In each iteration, I compared `lmax` and `rmax` to determine which side to move towards.
6. If `lmax` is less than `rmax`, I moved `p1` to the right, updating `lmax` and calculating the trapped water.
7. If `rmax` is less than or equal to `lmax`, I moved `p2` to the left, updating `rmax` and calculating the trapped water.
8. The loop continued until `p1` and `p2` crossed each other.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `height`.
  - The algorithm iterates through the array once using two pointers.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
