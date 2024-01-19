# Find the Duplicate Number 🧐

## Problem Statement

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

## Approach 🛠️

I've used Floyd's Tortoise and Hare algorithm to detect the cycle in a linked list to find the duplicate number.

1. Initialize two pointers, `slow` and `fast`, both pointing to the first element of the array.
2. Move `slow` one step at a time and `fast` two steps at a time.
3. If there is a cycle, `slow` and `fast` will meet at some point inside the cycle.
4. Reset one pointer (let's say `fast`) to the start of the array.
5. Move both pointers one step at a time until they meet again. The meeting point will be the start of the cycle.
6. The value at the meeting point is the duplicate number.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array.
  - The algorithm detects the cycle in a linked list.
- Space Complexity: O(1).
  - The algorithm uses constant extra space.
