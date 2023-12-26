# Linked List Cycle Detection 🔄

## Problem Statement

Given a linked list, determine if the linked list has a cycle in it.

A cycle is when a node's `next` point actually points back to an earlier node in the list.

**Example:**
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

## Approach 🛠️

I've used the Floyd's Tortoise and Hare algorithm to detect a cycle in the linked list.

1. I initialized two pointers, `slow` and `fast`, both pointing to the head of the linked list.
2. I used a while loop to iterate through the linked list.
3. In each iteration, `slow` moves one step at a time, while `fast` moves two steps at a time.
4. If there is no cycle, `fast` will reach the end of the linked list (`fast.next` or `fast.next.next` is `None`).
   - In this case, the function returns `False`.
5. If there is a cycle, the pointers will meet at some point within the cycle (`slow == fast`), and the function returns `True`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of nodes in the linked list.
  - The algorithm iterates through the linked list at most once.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
