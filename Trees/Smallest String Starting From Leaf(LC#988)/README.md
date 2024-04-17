# Finding the Smallest String from Leaf Nodes

## Problem Statement

Given the `root` of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba". A leaf of a node is a node that has no children.)

## Approach 🌟

To find the lexicographically smallest string starting from a leaf node and ending at the root, we can use depth-first search (DFS). Here's how we can approach this problem:

1. We traverse the binary tree using DFS, keeping track of the current string formed from the root to the current node.
2. During the traversal, when we reach a leaf node, we update the `smallest` string if the current string is lexicographically smaller than the current smallest string found so far.
3. Once we complete the DFS traversal, we return the smallest string found.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - We perform a depth-first traversal of the binary tree, visiting each node once.
- Space Complexity: O(H), where H is the height of the binary tree.
  - The space complexity is determined by the recursion stack during the depth-first traversal.
