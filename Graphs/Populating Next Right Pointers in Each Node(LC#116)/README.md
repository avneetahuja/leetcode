# Populate Next Right Pointers in Each Node 🌳

## Problem Statement

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `None`.

Initially, all next pointers are set to `None`.

## Approach 🌟

To populate the next pointers in each node, we can use a level-order traversal (BFS) of the binary tree. We maintain a queue to store the nodes at each level. 

1. Initialize an empty queue and enqueue the root node.
2. While the queue is not empty, iterate through each level:
    - Pop nodes from the queue one by one.
    - Connect each node to its next right node by setting the `next` pointer of the current node to the front element of the queue. 
    - Enqueue the left and right children of the current node (if they exist) for the next level.
3. Repeat this process until all levels are processed.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - Each node is visited once during the level-order traversal.
- Space Complexity: O(N), where N is the number of nodes in the binary tree (worst-case scenario).
  - The space complexity is dominated by the queue used for the BFS traversal.
