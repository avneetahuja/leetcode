# Binary Tree Inorder Traversal 🌳

## Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Approach 🛠️

The solution employs a recursive approach to perform an inorder traversal of the binary tree.

1. Initialize an empty list (`res`) to store the inorder traversal result.
2. Define a recursive function `inOrder` that takes a node as input and performs the following:
   - If the node is `None`, return.
   - Recursively call `inOrder` on the left subtree of the current node.
   - Append the value of the current node to the `res` list.
   - Recursively call `inOrder` on the right subtree of the current node.
3. Call the `inOrder` function with the root of the binary tree.
4. Return the `res` list containing the inorder traversal result.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the inorder traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the recursive call stack is proportional to the height of the tree.
