# Binary Tree Right Side View 🌳

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Approach 🛠️

The solution uses a depth-first traversal approach to find the right side view of the binary tree.

1. Define a helper function `addToRight` to traverse the tree in a depth-first manner.
2. In each recursive call, check if the current level is equal to the length of the `rightSide` list. If yes, it means we are visiting a new level for the first time. Add the value of the rightmost node at that level to the `rightSide` list.
3. Recursively call the function on the right and left subtrees.
4. The `rightSide` list contains the values of the rightmost nodes at each level, forming the right side view of the binary tree.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node once during the depth-first traversal.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space required for the recursive call stack is proportional to the height of the tree.
