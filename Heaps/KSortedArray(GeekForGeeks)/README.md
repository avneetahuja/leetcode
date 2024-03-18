# Nearly Sorted Algorithm 🔄🔍

## Problem Statement

Given an array of size N and an integer K, the task is to sort the array (in increasing order) such that:
- Each element in the sorted array is at most K distance away from its position in the original array.

## Approach 🚀

To solve this problem efficiently, we can use a min-heap to maintain a window of size K+1. We'll initialize the heap with the first K+1 elements of the array. Then, we'll perform the following steps:
1. Pop the smallest element from the heap and place it in its correct position in the array.
2. Add the next element from the array to the heap.
3. Repeat steps 1 and 2 until all elements are processed.

### Steps:
1. Create a min-heap `heap` and initialize it with the first K+1 elements of the array.
2. Iterate from index K to the end of the array, performing the following steps:
   - Pop the smallest element from the heap and place it at index i-K in the array.
   - Add the next element from the array to the heap.
3. After processing all elements, there might be elements left in the heap. Pop them and place them in their correct positions in the array.
4. Return the sorted array.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(K)), where N is the size of the array and K is the given integer.
  - Building the initial heap: O(K * log(K))
  - Each iteration of the loop: O(log(K))
- Space Complexity: O(K)
  - The space is used to store the heap of size K.
