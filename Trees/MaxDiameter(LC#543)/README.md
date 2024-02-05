# Diameter of Binary Tree 🌳🔍

## Problem Statement

Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## Approach 🛠️

The solution uses a recursive approach to calculate the diameter of the binary tree. It maintains a global variable (`maxD`) to keep track of the maximum diameter encountered during the traversal.

1. Define a helper function (`diam`) that takes a node as an argument and returns the height of the subtree rooted at the given node.
2. In the `diam` function:
   - If the node is `None` (i.e., it represents an empty subtree), return 0.
   - Recursively calculate the height of the left subtree (`lh`) and the right subtree (`rh`).
   - Update the maximum diameter (`maxD`) by considering the sum of the heights of the left and right subtrees.
   - Return the height of the current subtree (`1 + max(lh, rh)`).
3. In the `diameterOfBinaryTree` function (the main function for the problem):
   - Initialize the `maxD` variable to 0.
   - Call the `diam` function on the root of the binary tree.
   - Return the maximum diameter encountered (`self.maxD`).

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the call stack during the recursive calls is proportional to the height of the tree.
