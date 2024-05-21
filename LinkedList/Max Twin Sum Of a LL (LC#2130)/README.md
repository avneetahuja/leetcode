# Twin Sum in a Linked List

## Problem Description

You are given the head of a singly linked list. The list is made up of nodes where each node has a value and a reference to the next node. The list has an even number of nodes.

A twin sum is defined as the sum of values of a node and its twin node. The twin node of a node at position `i` in a 0-indexed list of length `n` is the node at position `n-1-i`.

Your task is to find the maximum twin sum in the list.

## Examples

### Example 1
- **Input:** `head = [5,4,2,1]`
- **Output:** `6`
- **Explanation:** The twin sums are (5 + 1) = 6 and (4 + 2) = 6. The maximum twin sum is 6.

### Example 2
- **Input:** `head = [4,2,2,3]`
- **Output:** `7`
- **Explanation:** The twin sums are (4 + 3) = 7 and (2 + 2) = 4. The maximum twin sum is 7.

## Approach

1. **Initial Check**:
    - If the list has only two nodes, directly return their sum.

2. **Find the Middle of the List**:
    - Use two pointers (`slow` and `fast`) to find the middle of the list. As `fast` pointer moves twice as fast as the `slow` pointer, when `fast` reaches the end of the list, `slow` will be at the middle.

3. **Store the First Half**:
    - As we traverse to find the middle, store the values of the first half in an array `sums`.

4. **Calculate Twin Sums**:
    - Continue traversing from the middle to the end of the list.
    - Sum each node's value with the corresponding value from the `sums` array.

5. **Find the Maximum Twin Sum**:
    - Track the maximum twin sum during the traversal.

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        
        slow, fast = head, head.next
        sums = [slow.val]
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            sums.append(slow.val)
        
        slow = slow.next
        i = len(sums) - 1
        
        while slow:
            sums[i] += slow.val
            i -= 1
            slow = slow.next
        
        return max(sums)
```

## Explanation

1. **Initial Check**:
    - If the list has exactly two nodes, return their sum.

2. **Finding the Middle**:
    - Initialize `slow` and `fast` pointers. Move `fast` twice as fast as `slow`.
    - Store the values of the nodes in the first half in the `sums` list.

3. **Calculating Twin Sums**:
    - After reaching the middle, continue with the `slow` pointer.
    - For each node from the middle to the end, add its value to the corresponding value in the `sums` array.

4. **Finding the Maximum**:
    - Track and return the maximum value from the `sums` array which now contains all the twin sums.

## Time Complexity
- The time complexity is O(n), where n is the number of nodes in the list. This is because we traverse the list twice: once to find the middle and once to calculate the twin sums.

## Space Complexity
- The space complexity is O(n/2) = O(n) because we store the first half of the node values in an array.
