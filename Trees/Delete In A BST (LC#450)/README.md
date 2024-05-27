# Delete Node in a Binary Search Tree

## Problem Description

Given the root of a binary search tree (BST) and an integer key, your task is to delete the node with the given key in the BST. Return the root of the modified BST.

The deletion can be summarized in three cases:
1. **Node to be deleted is a leaf**: Simply remove the node from the tree.
2. **Node to be deleted has only one child**: Replace the node with its child.
3. **Node to be deleted has two children**: Find the node's successor (smallest in the right subtree) or predecessor (largest in the left subtree), copy its value to the node, and recursively delete the successor or predecessor.

## Examples

### Example 1
- **Input**: root = [5,3,6,2,4,null,7], key = 3
- **Output**: [5,4,6,2,null,null,7]
- **Explanation**: Given key to delete is 3. So, we find the successor (4) and replace 3 with 4, then delete the successor.

### Example 2
- **Input**: root = [5,3,6,2,4,null,7], key = 0
- **Output**: [5,3,6,2,4,null,7]
- **Explanation**: Given key to delete is 0. Since it's not found in the tree, no changes are made.

### Example 3
- **Input**: root = [], key = 0
- **Output**: []
- **Explanation**: Given tree is empty, hence no changes.

## Approach

1. **Traversal and Search**:
    - Traverse the tree to find the node to be deleted.
    - Use the properties of BST where left child values are smaller and right child values are larger.

2. **Handling Different Cases**:
    - If the node to be deleted is found, handle the three cases (leaf node, one child, two children).

3. **Helper Functions**:
    - Define helper functions to find the successor and predecessor.

## Solution Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node
    
    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root).val
                root.left = self.deleteNode(root.left, root.val)
        
        return root
```

## Explanation

1. **Successor Function**:
    - To find the successor of a node (smallest value in the right subtree).

2. **Predecessor Function**:
    - To find the predecessor of a node (largest value in the left subtree).

3. **deleteNode Function**:
    - Traverse the tree to find the node with the given key.
    - Use the successor or predecessor to handle nodes with two children.
    - Update pointers to remove the node correctly.

## Complexity Analysis

- **Time Complexity**: O(h), where h is the height of the tree. In the worst case, this could be O(n) for a skewed tree.
- **Space Complexity**: O(h) due to the recursion stack.
