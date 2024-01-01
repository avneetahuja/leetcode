# Largest Rectangle in Histogram 📏

## Problem Statement

Given an array of non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

## Approach 🛠️

I've used a monotonic stack-based approach to find the largest rectangle in the histogram.

1. I created a stack to store pairs of indices and heights.
2. I iterated through the histogram array using a for loop.
3. In each iteration:
   - I compared the current height with the heights in the stack.
   - If the current height is smaller, I popped elements from the stack and calculated the area with respect to each popped height.
   - I maintained a variable `maxArea` to track the maximum area encountered so far.
   - I pushed the current index and height onto the stack.
4. After the loop, I processed any remaining elements in the stack to ensure no potential rectangles are left.
5. The final `maxArea` variable contains the area of the largest rectangle in the histogram.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `heights`.
  - The algorithm iterates through the histogram once.
- Space Complexity: O(n), where n is the length of the input array `heights`.
  - The space used by the stack is proportional to the number of elements in the histogram.
