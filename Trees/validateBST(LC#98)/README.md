# Validate Binary Search Tree 🌲

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with values less than the node's value.
- The right subtree of a node contains only nodes with values greater than the node's value.
- Both the left and right subtrees must also be valid BSTs.

## Approach 🛠️

The solution uses a recursive approach to validate whether a binary tree is a valid BST.

1. Define a recursive function `validate` that takes a node, along with the range (`left`, `right`) within which the node's value must lie.
2. If the current node is `None`, it is considered a valid BST.
3. Check whether the value of the current node falls within the range `(left, right)`. If not, the tree is not a valid BST.
4. Recursively check the left subtree, updating the range to `(left, node.val)`.
5. Recursively check the right subtree, updating the range to `(node.val, right)`.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution traverses each node once during the recursive validation process.
- Space Complexity: O(H), where H is the height of the binary tree (recursive call stack).
  - The maximum depth of the call stack is equal to the height of the tree.
