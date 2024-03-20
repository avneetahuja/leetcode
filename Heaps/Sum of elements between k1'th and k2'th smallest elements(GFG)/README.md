# Sum Between Two Kth Smallest Elements 📊

## Problem Statement

You are given an array `A` of size `N` and two integers `K1` and `K2`. Your task is to find the sum of all elements between the `K1`-th and `K2`-th smallest elements of the array.

## Approach 🚀

To find the sum of all elements between the `K1`-th and `K2`-th smallest elements of the array, we can use a min-heap. We'll start by pushing all the elements of the array into the min-heap. Then, we'll pop elements from the min-heap until we reach the `K1`-th smallest element. After that, we'll start summing the elements until we reach the `K2`-th smallest element.

### Steps:
1. Create an empty min-heap `heap` and heapify it.
2. Push all the elements from the array `A` into the min-heap.
3. Pop elements from the min-heap until we reach the `K1`-th smallest element.
4. Initialize a variable `s` to store the sum of elements, initially set to 0.
5. Iterate from `K1+1` to `K2-1`:
   - Add the popped element to `s`.
6. Return `s`.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(N)), where N is the size of the array `A`.
  - Building the min-heap: O(N * log(N))
  - Popping elements until `K1`-th smallest: O(K1 * log(N))
  - Summing elements between `K1`-th and `K2`-th smallest: O((K2 - K1) * log(N))
- Space Complexity: O(N)
  - We use additional space for the min-heap.
