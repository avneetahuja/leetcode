# Count Number of Occurrences in Sorted List 📊

## Problem Statement

Given a sorted array of integers `nums` and a target value, implement a binary search algorithm to count the number of occurrences of the target in the array.

## Approach 🛠️

I've implemented a binary search approach to find both the first and last occurrences of the target in the sorted array, and then calculated the count based on these indices.

1. I initialized two pointers, `l` and `r`, representing the left and right boundaries of the search for the first occurrence.
2. I iterated through the array while `l` was less than or equal to `r`.
3. In each iteration, I calculated the middle index, `m`, using `(l + r) // 2`.
4. I compared the target with the element at index `m`:
   - If they are equal, I updated `first = m` and continued the search in the left half by updating `r = m - 1`.
   - If the target is greater than the element at `m`, I updated `l = m + 1`.
   - If the target is less than the element at `m`, I updated `r = m - 1`.
5. After finding the first occurrence, I initialized `l` and `r` again for the search of the last occurrence.
6. I repeated the binary search for the last occurrence with the same logic, updating `last = m` and continuing the search in the right half by updating `l = m + 1`.
7. Finally, I returned the count of occurrences as `last - first + 1`.

## Complexity Analysis ⚙️

- Time Complexity: O(log n), where n is the length of the input array `nums`.
  - The binary search halves the search space in each iteration.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.

Feel free to customize this README further based on additional details you want to provide or any specific formatting preferences you have.
