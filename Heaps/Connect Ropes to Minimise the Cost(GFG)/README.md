# Min Cost of Connecting Ropes 🔗

## Problem Statement

You are given an array `arr` representing the lengths of `n` ropes. You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths. Your task is to find the minimum cost of connecting all the ropes into one rope.

## Approach 🚀

To find the minimum cost of connecting all the ropes into one rope, we can use a min-heap. We'll start by pushing all the rope lengths into the min-heap. Then, we'll repeatedly extract the two shortest ropes from the heap, connect them, and push the result back into the heap. We'll continue this process until there is only one rope left in the heap, which will be our final result.

### Steps:
1. Create an empty min-heap `heap` and heapify it.
2. Push all the rope lengths from the array `arr` into the min-heap.
3. Initialize a variable `total` to store the total cost, initially set to 0.
4. While the length of the heap is greater than 1, do the following:
   - Extract the two shortest ropes `a` and `b` from the heap.
   - Add the sum of `a` and `b` to the total cost.
   - Push the sum of `a` and `b` back into the heap.
5. Return the total cost.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(N)), where N is the number of ropes in the array `arr`.
  - Building the min-heap: O(N * log(N))
  - Extracting elements from the heap and pushing back: O(N * log(N))
- Space Complexity: O(N)
  - We use additional space for the min-heap.
