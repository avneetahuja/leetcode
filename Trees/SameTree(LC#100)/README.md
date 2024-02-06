# Same Tree Comparison 🌳🔄

## Problem Statement

Given the roots of two binary trees, `p` and `q`, determine if the trees are identical (i.e., they have the same structure and nodes have the same values).

## Approach 🛠️

The solution uses a recursive approach to compare two binary trees for structural and value equality.

1. Define a helper function (`compare`) that takes two nodes (`p` and `q`) as arguments and returns `True` if the trees rooted at `p` and `q` are identical, and `False` otherwise.
2. In the `compare` function:
   - If both `p` and `q` are `None`, return `True` (indicating the subtrees are identical).
   - If one of `p` or `q` is `None` (but not both), return `False` (indicating structural inequality).
   - If the values of `p` and `q` are not equal, return `False` (indicating value inequality).
   - Recursively compare the left subtrees (`p.left` and `q.left`) and the right subtrees (`p.right` and `q.right`).
3. In the `isSameTree` function (the main function for the problem):
   - Call the `compare` function with the root nodes of the given trees (`p` and `q`).
   - Return the result obtained from the `compare` function.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the larger of the two binary trees.
  - The solution visits each node exactly once during the recursive traversal.
- Space Complexity: O(H), where H is the height of the larger of the two binary trees.
  - The space used by the call stack during the recursive calls is proportional to the height of the larger tree.
