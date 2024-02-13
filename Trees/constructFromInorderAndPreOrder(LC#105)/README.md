# Build Binary Tree from Preorder and Inorder Traversal 🌲

## Problem Statement 🚧

Given two arrays representing the preorder and inorder traversal sequences of a binary tree, construct the binary tree.

## Approach 🛠️

We can solve this problem using a recursive approach. Starting with the root, we can identify the root node from the preorder list and then recursively build the left and right subtrees using the corresponding portions of the inorder list.

1. **Base Case:** If either the preorder or inorder list is empty, return `None`.
2. **Root Node:** Create the root node using the first element of the preorder list.
3. **Root Index:** Find the index of the root value in the inorder list.
4. **Build Left Subtree:** Recursively build the left subtree using the portions of the preorder and inorder lists related to the left subtree.
5. **Build Right Subtree:** Recursively build the right subtree using the portions of the preorder and inorder lists related to the right subtree.
6. **Return Root:** Return the constructed root node.

## Complexity Analysis ⚙️

The time complexity of this approach is O(N), where N is the total number of nodes in the binary tree. This is because each node is processed exactly once.

The space complexity is O(N), considering the space required for recursive function calls on the call stack.
