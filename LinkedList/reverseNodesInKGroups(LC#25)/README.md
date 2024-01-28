# Reverse Nodes in k-Group 🔄

## Problem Statement

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Approach 🛠️

The solution uses a dummy node to simplify the reversal process and iterates through the linked list in k-sized groups. It employs a helper function `getKth` to find the kth node from the current position. For each group, it reverses the nodes within the group and updates pointers accordingly.

1. Initialize a dummy node (`dummy`) with the next pointing to the head of the linked list.
2. Create a pointer (`groupPrev`) to the dummy node for keeping track of the previous group's last node.
3. Iterate through the linked list in k-sized groups:
   - Find the kth node (`kth`) using the `getKth` helper function.
   - If there are fewer than k nodes remaining, break the loop.
   - Set `groupNext` to the next node after the kth node.
   - Reverse the nodes in the current group:
     - Use `prev` and `curr` pointers to reverse the group in-place.
   - Update pointers to connect the reversed group:
     - Connect the last node of the previous group to the first node of the reversed group.
     - Set `groupPrev` to the first node of the original group before reversal.
4. Return the modified list, starting from the dummy node's next.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of nodes in the linked list.
  - The solution iterates through each node once.
- Space Complexity: O(1).
  - The solution uses a constant amount of extra space.
