# Kth Largest Element in an Array 📊

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note: You are not allowed to sort the array to solve the problem.

## Approach 🚀

To find the `kth` largest element in the array, we can use a min-heap of size `k`. We'll iterate through each element in the `nums` array and maintain a min-heap containing the `k` largest elements encountered so far. At any point, if the size of the heap exceeds `k`, we'll remove the smallest element from the heap.

### Steps:
1. Create an empty min-heap `heap`.
2. Iterate through each element `n` in the `nums` array, and for each element do the following:
   - Push the element onto the min-heap.
   - If the size of the min-heap exceeds `k`, pop the smallest element from the heap.
3. After processing all elements, the `kth` largest element will be the root of the min-heap.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(K)), where N is the number of elements in the `nums` array and K is the given integer `k`.
  - Building the min-heap: O(N * log(K))
  - Extracting the `kth` largest element: O(K * log(K))
- Space Complexity: O(K)
  - The space is used to store the min-heap of size `k`.
