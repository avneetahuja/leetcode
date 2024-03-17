# Kth Largest Element in a Stream 🔢💡

## Problem Statement

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement `KthLargest` class with the following API:

- `KthLargest(int k, int[] nums)`: Initializes the object with the integer k and the stream of integers nums.
- `int add(int val)`: Appends the integer val to the stream and returns the kth largest element in the stream.

## Approach 🚀

To solve this problem efficiently, we can use a min-heap to maintain the k largest elements seen so far. The heap will always contain the k largest elements, with the smallest of these elements at the root.

### Steps:
1. Initialize the class with the value of k and the initial list of integers nums.
2. Create a min-heap `heap` from the given list of integers `nums`.
3. While the length of `heap` is greater than `k`, pop the smallest element from the heap using `heapq.heappop()`.
4. When adding a new element `val`, push it onto the heap using `heapq.heappush()`.
5. If the length of `heap` exceeds `k`, remove the smallest element from the heap using `heapq.heappop()`.
6. Return the root element of the heap, which will be the kth largest element.

## Complexity Analysis ⚙️

- Time Complexity:
  - Initialization: O(N * log(k)), where N is the number of elements in the initial list and log(k) is the complexity of heap operations.
  - Adding a new element: O(log(k)), where k is the size of the heap.
- Space Complexity: O(k)
  - The space is used to store the k largest elements in the min-heap.
