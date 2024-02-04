# Maximum Depth of Binary Tree 🌲🚀

## Problem Statement

Given the root of a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Approach 🛠️

The solution utilizes a recursive approach to calculate the maximum depth of the binary tree.

1. Define a recursive function (`maxD`) that takes a node as an argument and returns the maximum depth of the subtree rooted at that node.
2. In the `maxD` function:
   - If the node is `None` (i.e., it represents an empty subtree), return 0.
   - Calculate the maximum depth of the left subtree (`l`) by recursively calling `maxD` on the left child of the current node.
   - Calculate the maximum depth of the right subtree (`r`) by recursively calling `maxD` on the right child of the current node.
   - Return `1 + max(l, r)`, representing the maximum depth of the current subtree.
3. In the `maxDepth` function (the main function for the problem):
   - Return the result of calling `maxD` with the root of the binary tree.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the call stack during the recursive calls is proportional to the height of the tree.
