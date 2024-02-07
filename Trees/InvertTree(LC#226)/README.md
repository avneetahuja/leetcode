# Invert Binary Tree 🌳🔄

## Problem Statement

Given the root of a binary tree, invert the tree (mirror the tree).

## Approach 🛠️

The solution uses a recursive approach to invert the binary tree.

1. Define a helper function (`swap`) that takes a node as an argument and swaps its left and right subtrees.
2. In the `swap` function:
   - If the node is `None`, return.
   - Swap the left and right subtrees of the current node.
   - Recursively call the `swap` function on the left and right subtrees.
3. In the `invertTree` function (the main function for the problem):
   - Call the `swap` function with the root node of the given tree.
   - Return the root node after inversion.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the call stack during the recursive calls is proportional to the height of the tree.
