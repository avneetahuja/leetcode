# Moving Average from Data Stream 📈

## Problem Statement

You are given a stream of integers and a window size `size`, where you need to calculate the moving average of all integers in the sliding window.

Design a class `MovingAverage` that supports the following operations:
- `MovingAverage(size)`: Initializes the object with the size of the window.
- `next(val)`: Returns the moving average of the last `size` values.

## Approach 📈

To solve this problem, we can use a deque (double-ended queue) to store the stream of integers. We maintain the window size by removing elements from the deque when the size exceeds the specified limit. To calculate the moving average, we sum up the elements in the deque and divide by the number of elements.

### Steps:
1. Initialize a deque `stream` to store the stream of integers and a variable `size` to store the window size.
2. In the constructor `__init__`, initialize the `stream` and `size` variables.
3. In the `next` method, append the new value to the left end of the deque.
4. If the length of the deque exceeds the window size, remove elements from the right end of the deque until the size becomes equal to the specified window size.
5. Calculate the moving average by summing up the elements in the deque and dividing by the number of elements.
6. Return the calculated moving average.

## Complexity Analysis ⚙️

- Time Complexity:
  - Initialization: O(1)
  - Adding a new element: O(1)
  - Removing elements exceeding the window size: O(1)
  - Calculating the moving average: O(N), where N is the window size
- Space Complexity: O(N)
  - We use a deque to store the stream of integers, which can have up to N elements.
