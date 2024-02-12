# Count Good Nodes in Binary Tree 🌳

## Problem Statement

Given a binary tree, return the number of nodes that are "good nodes."

A node is considered "good" if, in the path from the root to the node, there are no nodes with a value greater than the node's value.

## Approach 🛠️

The solution uses a recursive depth-first search (DFS) to traverse the binary tree and count the "good nodes."

1. Initialize a counter variable (`goodCount`) to keep track of the number of good nodes.
2. Start the DFS traversal from the root of the binary tree.
3. For each node visited, compare its value with the maximum value encountered in the path from the root to the current node.
4. If the node's value is greater than or equal to the maximum value, update the maximum value and increment the `goodCount`.
5. Recursively visit the left and right children of the current node.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution traverses each node once during the depth-first search.
- Space Complexity: O(H), where H is the height of the binary tree (recursive call stack).
  - The solution uses a recursive approach, and the maximum depth of the call stack is equal to the height of the tree.
