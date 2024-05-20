# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head
        odd,even_head,even,ptr = head,head.next,head.next,head.next.next
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
