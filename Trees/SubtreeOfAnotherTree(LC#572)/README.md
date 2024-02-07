# Subtree of Another Tree 🌳🌲

## Problem Statement

Given two non-empty binary trees `root` and `subRoot` consisting of unique values, check whether `subRoot` is a subtree of `root`.

A subtree of a tree `T` is a tree consisting of a node `V` in `T` and all of `V`'s descendants from `T`. The tree `T` could also be considered as a subtree of itself.

## Approach 🛠️

The solution uses a recursive approach to check if `subRoot` is a subtree of `root`.

1. Define two helper functions (`preOrderRoot` and `preOrderSubRoot`) to perform pre-order traversal of the trees and generate string representations.
   - In the string representation, the null nodes are represented as "null," and the values of nodes are separated by a dot ('.') to avoid cases where one node is a prefix of another.
2. In the `isSubtree` function (the main function for the problem):
   - Initialize two empty strings (`res` and `res2`) to store the pre-order string representations of `root` and `subRoot`.
   - Call `preOrderRoot` with the `root` and `preOrderSubRoot` with `subRoot` to generate the string representations.
   - Check if `res2` is a substring of `res` to determine if `subRoot` is a subtree of `root`.
   - Return `True` if it is a subtree; otherwise, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(M * N), where M is the number of nodes in `root` and N is the number of nodes in `subRoot`.
  - The solution performs a pre-order traversal of both trees and compares the string representations.
- Space Complexity: O(M + N), where M is the number of nodes in `root` and N is the number of nodes in `subRoot`.
  - The space used by the string representations.
