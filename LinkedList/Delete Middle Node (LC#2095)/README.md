# Delete the Middle Node of a Linked List

## Problem Description

Given the head of a singly linked list, write a function to delete the middle node of the linked list and return the head of the modified list. If the list has only one node, return `None`.

The middle node of a linked list with `n` nodes is the `(n // 2)th` node (0-indexed). For example, the middle node of a list with `5` nodes is the node at index `2` (0-based).

## Approach

1. **Edge Cases**: 
    - If the list has only one node, return `None`.
    - If the list has two nodes, remove the second node.

2. **Two-pointer Technique**:
    - Use a slow pointer (`slow`) and a fast pointer (`fast`). Initialize `slow` at the second node and `fast` at the third node.
    - Maintain a `slow_prev` pointer to keep track of the node before `slow`.
    - Move `slow` one step and `fast` two steps in each iteration.
    - When `fast` reaches the end of the list, `slow` will be at the middle node.

3. **Delete the Middle Node**:
    - Adjust the `next` pointer of `slow_prev` to skip the middle node (`slow`).

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head
        
        slow_prev, slow, fast = head, head.next, head.next.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow_prev = slow
            slow = slow.next
        
        if fast.next:
            slow_prev = slow
            slow = slow.next
        
        slow_prev.next = slow.next
        return head
```

## Explanation

1. **Initial Check**:
    - If the list has only one node, return `None`.
    - If the list has two nodes, remove the second node by setting `head.next` to `None`.

2. **Initialize Pointers**:
    - `slow_prev` starts at the head, `slow` at the second node, and `fast` at the third node.

3. **Move Pointers**:
    - Move `slow` by one step and `fast` by two steps until `fast` reaches the end.
    - Update `slow_prev` to the current position of `slow` before moving `slow`.

4. **Delete Middle Node**:
    - Set the `next` pointer of `slow_prev` to the node after `slow`, effectively removing `slow` from the list.

## Time Complexity
- The time complexity is O(n), where n is the number of nodes in the linked list, because each node is processed at most twice.

## Space Complexity
- The space complexity is O(1) because only a fixed amount of extra space is used regardless of the input size.
