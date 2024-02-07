# Lowest Common Ancestor of a Binary Search Tree (LCA in BST) 🌲

## Problem Statement

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on [Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):
"The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Approach 🛠️

The solution uses a simple iterative approach to find the LCA of nodes `p` and `q` in the BST.

1. Iterate through the tree using a `while` loop:
   - If both `p` and `q` are greater than the current node's value, move to the right subtree.
   - If both `p` and `q` are less than the current node's value, move to the left subtree.
   - If the current node's value is between `p` and `q`, return the current node as it is the LCA.

## Complexity Analysis ⚙️

- Time Complexity: O(log N), where N is the number of nodes in the BST.
  - In each iteration of the `while` loop, the search space is reduced by half.
- Space Complexity: O(1)
  - The solution uses only a constant amount of space.
