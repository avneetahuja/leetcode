# Merge Two Sorted Lists 🔄

## Problem Statement

Merge two sorted linked lists and return it as a new sorted list.

## Approach 🛠️

I've implemented the iterative approach to merge two sorted linked lists. Here are the key steps:

1. I compare the values of the current nodes from both lists and connect the smaller node to the merged list.
2. I update the current pointer to the node that was connected.
3. I continue this process until one of the lists becomes empty.
4. If one of the lists is not empty, I connect the remaining nodes to the merged list.

## Complexity Analysis ⚙️

- Time Complexity: O(n + m), where n and m are the lengths of the two input lists.
  - I iterate through both lists once.
- Space Complexity: O(1), as no additional space is used.
