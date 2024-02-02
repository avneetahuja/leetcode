# Binary Tree Level Order Traversal 🌳🚀

## Problem Statement

Given the root of a binary tree, return its level order traversal, where the nodes' values are grouped by level.

## Approach 🛠️

The solution uses a breadth-first traversal (BFS) approach to traverse the binary tree level by level.

1. Initialize an empty list (`res`) to store the level order traversal result.
2. Initialize an empty queue (`q`) to perform the BFS.
3. Enqueue the root of the binary tree into the queue if it exists.
4. While the queue is not empty:
   - Initialize an empty list (`vals`) to store the values at the current level.
   - Iterate through the nodes in the current level (the number of nodes in the queue at the beginning of the iteration):
     - Dequeue the front node from the queue.
     - Append the value of the node to the `vals` list.
     - Enqueue the left and right children of the node if they exist.
   - Append the `vals` list to the `res` list.
5. Return the `res` list containing the level order traversal result.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution visits each node exactly once during the BFS traversal.
- Space Complexity: O(W), where W is the maximum width (number of nodes at any level) of the binary tree.
  - The space used by the queue is proportional to the maximum width of the tree.
