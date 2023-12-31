# Next Greater Element II 🔄🔍

## Problem Statement

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the next greater number for every element in `nums`.

The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

## Approach 🛠️

I've used a monotonic stack-based approach to find the next greater elements in a circular array.

1. I created an array `answer` initialized with `-1` to store the results.
2. I concatenated `nums` with itself to simulate the circular array.
3. I used a stack to store elements along with their indices.
4. I iterated through the concatenated array using a for loop.
5. In each iteration:
   - I compared the current element `n` with elements in the stack, and if `n` is greater, I updated the `answer` array for the corresponding indices.
   - I pushed the current element and its index onto the stack.
6. The final `answer` array contains the next greater elements for each element in the circular array.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through the array once.
- Space Complexity: O(n), where n is the length of the input array `nums`.
  - The space used by the stack is proportional to the number of elements in the array.
