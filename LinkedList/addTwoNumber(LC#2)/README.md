# Add Two Numbers 🧮

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Approach 🛠️

I've used a simple iterative approach to traverse both linked lists, add corresponding digits, and maintain carry. The result is represented as a linked list.

1. Initialize a dummy node to represent the head of the result linked list.
2. Traverse both input linked lists simultaneously.
3. For each pair of nodes, add their values along with the carry from the previous step.
4. Update the carry for the next iteration and create a new node with the result's least significant digit.
5. Move to the next nodes in both input lists and the result list.
6. Continue this process until both input lists are exhausted.
7. If there is a carry left after traversing both lists, add a new node with the carry to the result list.
8. The final result is represented by the next of the dummy node.

## Complexity Analysis ⚙️

- Time Complexity: O(max(n, m)), where n and m are the lengths of the input linked lists.
  - The algorithm traverses both linked lists once.
- Space Complexity: O(max(n, m)), where n and m are the lengths of the input linked lists.
  - The space required for the result linked list is proportional to the maximum length of the input lists.
