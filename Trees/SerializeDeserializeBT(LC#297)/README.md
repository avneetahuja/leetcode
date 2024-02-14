# Serialize and Deserialize Binary Tree 📦🌳

## Problem Statement

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Note:** Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later.

## Approach 🛠️

The solution uses a pre-order traversal for both serialization and deserialization.

1. **Serialization (`serialize` method):**
   - Perform a pre-order traversal of the tree.
   - Append the node values to a string, separating them with commas.
   - Use 'N' to represent `None` values.
   - Return the serialized string.

2. **Deserialization (`deserialize` method):**
   - Split the serialized string into a list of node values.
   - Initialize an index to keep track of the current position in the list.
   - Define a helper function (`build`) for recursive deserialization.
   - In the `build` function:
     - If the current node value is 'N', return `None`.
     - Create a new node with the current value.
     - Recursively build the left and right subtrees.
   - Return the root of the reconstructed binary tree.

## Complexity Analysis ⚙️

- **Time Complexity:**
  - Serialization: O(N), where N is the number of nodes in the binary tree (each node is visited once).
  - Deserialization: O(N), where N is the number of nodes in the binary tree (each node is visited once).
- **Space Complexity:**
  - Serialization: O(N), the space required for the serialized string.
  - Deserialization: O(H), where H is the height of the binary tree (space used by the call stack during recursion).
