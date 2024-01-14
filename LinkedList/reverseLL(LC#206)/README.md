# Reverse Linked List 🔗

## Problem Statement

Given the head of a singly-linked list, reverse the list and return its head.

## Approach 🛠️

I've implemented the iterative approach to reverse a linked list. Here are the key steps:

1. I maintain two pointers: `curr` and `prev`.
2. I iterate through the linked list, updating the `next` pointers of each node to reverse the direction.
3. After reversing the list, I update the `head` pointer to the new head of the reversed list (`prev`).

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of nodes in the linked list.
  - I iterate through the list once.
- Space Complexity: O(1), as no additional space is used.
