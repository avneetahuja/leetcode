# Remove Nth Node From End of List 🗑️

## Problem Statement

Given the head of a linked list, remove the n-th node from the end of the list and return its head.

## Approach 🛠️

I've used a two-pointer approach to find and remove the n-th node from the end:

1. I use two pointers, `left` and `right`, initially pointing to the head.
2. I move the `right` pointer ahead by n nodes.
3. Then, I move both `left` and `right` pointers until `right` reaches the end of the list.
4. Finally, I update the `next` pointer of the node pointed to by `left` to skip the n-th node.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the linked list.
  - The algorithm iterates through the linked list twice.
- Space Complexity: O(1), as no additional space is used.
