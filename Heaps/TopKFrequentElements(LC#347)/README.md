# Top K Frequent Elements 🔝

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Approach 🚀

To find the `k` most frequent elements, we can use a combination of a frequency map and a min-heap.

### Steps:
1. Create an empty frequency map `map`.
2. Iterate through each element `n` in the `nums` array, and for each element do the following:
   - Update the frequency count of `n` in the frequency map.
3. Create an empty min-heap `heap`.
4. Iterate through each key-value pair `(key, val)` in the frequency map, and for each pair do the following:
   - Push the pair `(val, key)` onto the min-heap.
   - If the size of the min-heap exceeds `k`, pop the smallest element from the heap.
5. After processing all key-value pairs, the `k` most frequent elements will be the elements present in the min-heap.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(K)), where N is the number of elements in the `nums` array and K is the given integer `k`.
  - Building the frequency map: O(N)
  - Building the min-heap: O(N * log(K))
  - Extracting the `k` most frequent elements: O(K * log(K))
- Space Complexity: O(N + K)
  - The space is used to store the frequency map and the min-heap of size `k`.
