# Daily Temperatures 🌡️

## Problem Statement

Given a list of daily temperatures, where `temperatures[i]` is the temperature of the i-th day, find the number of days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

## Approach 🛠️

I've used a monotonic stack approach to find the number of days until a warmer temperature.

1. I initialized an array `answer` of the same length as the input list `temperatures` to store the results.
2. I initialized an empty stack to keep track of indices of temperatures.
3. I iterated through the temperatures using a for loop.
4. In each iteration:
   - While the stack is not empty and the current temperature is greater than the temperature at the top of the stack:
      - I updated the result for the temperature at the top of the stack with the difference in indices.
      - I popped the top element from the stack.
   - I pushed the current temperature and its index onto the stack.
5. The final result was the `answer` array containing the number of days until a warmer temperature for each day.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input list `temperatures`.
  - The algorithm iterates through the list once.
- Space Complexity: O(n), where n is the length of the input list `temperatures`.
  - The space used by the stack is proportional to the length of the input list.
