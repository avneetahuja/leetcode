# Last Stone Weight 🪨💪

## Problem Statement

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

- If x == y, both stones are totally destroyed;
- If x != y, the stone of weight x is totally destroyed, and the stone of weight y has a new weight y - x.

At the end, there is at most one stone left. Return the weight of this stone (or 0 if there are no stones left.)

## Approach 🚀

To solve this problem efficiently, we can use a max-heap to store the weights of the stones. We'll iterate until we have one or zero stones left, smashing the two heaviest stones together on each turn.

### Steps:
1. Negate the weights of the stones and create a max-heap `stones` using `heapq.heapify()`.
2. While the length of `stones` is greater than 1, perform the following steps:
   - Pop the two heaviest stones from the max-heap using `heapq.heappop()`.
   - Calculate the difference between the weights of the two stones and push the result back into the max-heap using `heapq.heappush()`.
3. Return the weight of the last stone, which will be the only stone left in the heap.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(N)), where N is the number of stones.
  - Building the heap: O(N * log(N))
  - Each iteration of the while loop: O(log(N))
- Space Complexity: O(N)
  - The space is used to store the weights of the stones in the max-heap.
