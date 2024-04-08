# Level Order Traversal of N-ary Tree 🌳

## Problem Statement

Given an n-ary tree, return the level order traversal of its nodes' values.

N-ary Tree is a tree in which each node has no more than N children.

## Approach 🌟

To perform level order traversal of an n-ary tree, we can use Breadth-First Search (BFS) algorithm.

1. Start from the root node and perform BFS.
2. Use a queue to keep track of nodes to visit next.
3. Initialize an empty list `res` to store the result.
4. Iterate through the queue while it's not empty:
    - Pop a node from the queue.
    - Append the value of the node to the current level list.
    - Enqueue all children of the node.
5. Append the current level list to the result list.
6. Repeat steps 4-5 until the queue is empty.
7. Return the result list containing the level order traversal.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the n-ary tree.
  - Each node is visited exactly once during BFS.
- Space Complexity: O(N), where N is the number of nodes in the n-ary tree.
  - The space complexity is dominated by the queue used in BFS.
