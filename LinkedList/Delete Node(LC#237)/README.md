# Delete Node in a Linked List 🗑️

## Problem Statement

You are given a pointer to the node that you need to delete. You are not given access to the head of the linked list.

Write a function to delete the node (except the tail) in a singly linked list, given only access to that node.

## Approach 🚀

To delete a node from a singly linked list when you only have access to that node:
1. Copy the value of the next node to the current node.
2. Update the current node's `next` pointer to skip the next node (effectively removing it).

### Steps:
1. Iterate through the linked list until the next node is `None`.
2. For each node, copy the value of the next node to the current node and move to the next node.
3. Once the next node is `None`, update the `next` pointer of the previous node to `None`.

## Complexity Analysis ⚙️

- Time Complexity: O(1)
  - Since we are only modifying the pointers of the current node and its next node, the time complexity is constant.
- Space Complexity: O(1)
  - We are using only constant space for variables.
