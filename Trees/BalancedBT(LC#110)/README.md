# Balanced Binary Tree 🌳⚖️

## Problem Statement

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as:

> A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## Approach 🛠️

The solution employs a recursive approach to check whether a binary tree is balanced or not.

1. Define a helper function (`heightAndBalanced`) that takes a node as an argument and returns two values:
   - The height of the subtree rooted at the given node.
   - A boolean indicating whether the subtree is balanced or not.
2. In the `heightAndBalanced` function:
   - If the node is `None` (i.e., it represents an empty subtree), return [0, True] since an empty tree is considered balanced.
   - Recursively calculate the height and balanced status of the left subtree (`l`) and the right subtree (`r`).
   - Check if the current subtree is balanced based on the conditions:
     - The left subtree is balanced (`l[1]` is `True`).
     - The right subtree is balanced (`r[1]` is `True`).
     - The absolute difference in heights of the left and right subtrees is at most 1.
   - Return the height of the current subtree (`1 + max(l[0], r[0])`) and the boolean indicating whether it is balanced or not.
3. In the `isBalanced` function (the main function for the problem):
   - Return the balanced status (`heightAndBalanced(root)[1]`).

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the call stack during the recursive calls is proportional to the height of the tree.
