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
        
