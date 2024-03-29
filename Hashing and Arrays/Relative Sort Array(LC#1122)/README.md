# Relative Sort Array 📊

## Problem Statement

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that don't appear in `arr2` should be placed at the end of `arr1` in ascending order.

## Approach 🚀

To solve this problem, we can use a two-step approach:

1. Create a dictionary (`map`) to store the indices of elements in `arr2`.
2. Iterate through `arr1`:
   - If the element is present in `arr2`, place it in the corresponding sublist of `li`.
   - If the element is not present in `arr2`, place it in the last sublist of `li`.
3. Sort the elements in the last sublist of `li`.
4. Concatenate all sublists in `li` to obtain the sorted array.

## Complexity Analysis ⚙️

- Time Complexity: O(n * log n)
  - Sorting the elements in the last sublist takes O(n * log n) time.
- Space Complexity: O(n)
  - We use additional space for the `map` and `li` lists.
