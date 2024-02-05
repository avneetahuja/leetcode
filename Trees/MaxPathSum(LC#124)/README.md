# Maximum Path Sum in Binary Tree 🌳🔍

## Problem Statement

Given the root of a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

## Approach 🛠️

The solution uses a recursive approach to find the maximum path sum in a binary tree. It maintains a global variable (`res`) to keep track of the maximum path sum encountered during the traversal.

1. Define a helper function (`findMaxSum`) that takes a node as an argument and returns the maximum path sum that can be formed by including the current node in the path.
2. In the `findMaxSum` function:
   - If the node is `None` (i.e., it represents an empty subtree), return 0.
   - Recursively calculate the maximum path sum in the left subtree (`l`) and the right subtree (`r`).
   - Update the maximum path sum (`res`) by considering the sum of values from the left and right subtrees and the current node's value.
   - Return the maximum path sum that can be formed by including either the current node alone or with one of its subtrees (`node.val + max(l, r)`).
3. In the `maxPathSum` function (the main function for the problem):
   - Initialize the `res` variable to the value of the root node.
   - Call the `findMaxSum` function on the root of the binary tree.
   - Return the maximum path sum encountered (`self.res`).

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space used by the call stack during the recursive calls is proportional to the height of the tree.
