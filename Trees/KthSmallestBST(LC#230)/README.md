# Kth Smallest Element in a BST 🌲

## Problem Statement

Given the root of a binary search tree (BST), return the kth smallest element in it.

Note: Kth smallest element is the kth element in the sorted order, not the kth distinct element.

## Approach 🛠️

The solution employs an in-order traversal of the BST to gather the elements in ascending order. The kth element in the resulting list is then returned as the answer.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the BST.
  - The solution performs an in-order traversal, visiting each node exactly once.
- Space Complexity: O(N), where N is the number of nodes in the BST.
  - The solution uses a list to store the elements in sorted order.
