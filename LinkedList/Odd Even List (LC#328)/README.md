# Odd Even Linked List

## Problem Description

Given a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The relative order inside both the even and odd groups should remain as it was in the input.

The first node is considered odd, and the second node is even, and so on.

## Examples

### Example 1
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[1,3,5,2,4]`

### Example 2
- **Input:** `head = [2,1,3,5,6,4,7]`
- **Output:** `[2,3,6,7,1,5,4]`

## Approach

1. **Initial Check**:
    - If the list is empty or has less than three nodes, return the head as it is.

2. **Initialize Pointers**:
    - `odd`: Points to the head of the odd indexed nodes.
    - `even_head`: Points to the head of the even indexed nodes.
    - `even`: Used to traverse and link even indexed nodes.
    - `ptr`: Used to traverse the entire list starting from the third node.
    - `isEven`: A flag to toggle between odd and even nodes.

3. **Traverse the List**:
    - Use `ptr` to iterate through the list.
    - Use `isEven` flag to determine if the current node is odd or even.
    - Link nodes appropriately to `odd` or `even` lists.
    - Toggle the `isEven` flag after processing each node.

4. **Connect Odd and Even Lists**:
    - After traversing all nodes, link the end of the odd list to the head of the even list.
    - Ensure the end of the even list points to `None`.

5. **Return the Modified List**:
    - Return the head of the modified list which starts with odd indexed nodes followed by even indexed nodes.

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head
        
        odd, even_head, even, ptr = head, head.next, head.next, head.next.next
        isEven = False
        
        while ptr:
            if not isEven:
                odd.next = ptr
                odd = ptr
            else:
                even.next = ptr
                even = ptr
            ptr = ptr.next
            isEven = not isEven
        
        even.next = None
        odd.next = even_head

        return head
```

## Explanation

1. **Initial Check**:
    - If the linked list has less than three nodes, the arrangement is already as required.

2. **Pointer Initialization**:
    - `odd` is initialized to the head (first node).
    - `even_head` and `even` are initialized to the second node.
    - `ptr` is initialized to the third node.
    - `isEven` is initialized to `False` to indicate the third node is odd.

3. **Traversal and Linking**:
    - Traverse the list with `ptr`.
    - Depending on the value of `isEven`, append nodes to either `odd` or `even`.
    - Toggle `isEven` after processing each node.

4. **Final Adjustments**:
    - Terminate the even list by setting `even.next` to `None`.
    - Append the even list to the end of the odd list by setting `odd.next` to `even_head`.

5. **Return Result**:
    - Return the modified list starting from the head.

## Time Complexity
- The time complexity is O(n), where n is the number of nodes in the linked list because we traverse each node exactly once.

## Space Complexity
- The space complexity is O(1) since no additional space is used except for a few pointers.
