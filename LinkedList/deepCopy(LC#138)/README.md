# Copy List with Random Pointer 🧠

## Problem Statement

A linked list is given such that each node contains an additional random pointer, which could point to any node in the list or null.

Return a deep copy of the list.

## Approach 🛠️

I've used a three-step approach to create a deep copy of the linked list:

1. **Duplicate Nodes:** Traverse the original linked list and duplicate each node. Insert the duplicated node right after the original node.

2. **Copy Random Pointers:** Update the random pointers of the duplicated nodes to point to the corresponding duplicated nodes.

3. **Extract Duplicated List:** Separate the original list and the duplicated list, restoring the original list and returning the duplicated list.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the linked list.
  - The algorithm traverses the linked list three times: for duplication, for updating random pointers, and for extraction.
- Space Complexity: O(1), as no additional space is used except for variables.
