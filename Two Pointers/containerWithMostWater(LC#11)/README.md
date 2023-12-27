# Container With Most Water 📈💦

## Problem Statement

Given `n` non-negative integers `height` where each represents the height of a vertical line chart, find two lines that form a container, such that it contains the most water.

**Example:**
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing the indices 1 and 8, forming a container with a height of 7 and a width of 7 (7 * 7 = 49).

## Approach 🛠️

I've used a two-pointer approach to find the maximum area of a container formed by two vertical lines.

1. I initialized two pointers `p1` and `p2` at the beginning and end of the array, respectively.
2. I initialized a variable `maxA` to store the maximum area.
3. I used a while loop to iterate through the array.
4. In each iteration, I calculated the area formed by the lines at `p1` and `p2`.
5. I updated `maxA` with the maximum of the current area and the previous maximum.
6. I moved the pointers based on the height of the lines, always keeping the pointer associated with the shorter line.
7. The loop continued until the pointers met.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `height`.
  - The algorithm iterates through the array using two pointers.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
