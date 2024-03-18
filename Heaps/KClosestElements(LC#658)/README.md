# Find K Closest Elements to a Given Value 🎯

## Problem Statement

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

## Approach 🚀

To solve this problem efficiently, we can use a max-heap to maintain the `k` closest elements to the target value `x`. We'll iterate through the array, calculating the absolute difference between each element and `x` and storing the negative of the absolute difference along with the element value in the max-heap.

### Steps:
1. Create a max-heap `heap`.
2. Iterate through the array `arr` and for each element `n`, do the following:
   - Calculate the absolute difference between `x` and `n`.
   - Push the tuple `(-abs(x - n), -n)` onto the max-heap.
   - If the size of the max-heap exceeds `k`, pop the largest element.
3. After processing all elements, extract the elements from the max-heap and sort them to get the result.
4. Return the sorted `k` closest elements to `x`.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(K)), where N is the size of the array `arr` and K is the given integer `k`.
  - Building the max-heap: O(N * log(K))
  - Extracting and sorting the result: O(K * log(K))
- Space Complexity: O(K)
  - The space is used to store the max-heap of size `k`.
