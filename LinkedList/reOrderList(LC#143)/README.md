# Reorder List 🔄

## Problem Statement

Given a singly linked list, reorder its nodes in-place such that they alternate between the smallest and largest nodes. You should not modify the values in the nodes, only their order.

## Approach 🛠️

I've used a two-step approach to reorder the list:

1. **Find the middle of the linked list**: I use the slow and fast pointers to find the middle of the linked list.
2. **Reverse the second half of the linked list**: I reverse the second half of the linked list starting from the middle.
3. **Merge the two halves**: I merge the first and reversed second halves to achieve the desired reordering.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the linked list.
  - The algorithm involves finding the middle (O(n/2)) and reversing the second half (O(n/2)).
- Space Complexity: O(1), as no additional space is used.
