# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        slow = head
        fast =head.next
        while(fast.next):
            if not fast.next.next:
                fast=fast.next
            else:
                fast=fast.next.next
            slow=slow.next

        curr=slow.next
        prev= None
        slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        p1 = head
        while prev:
            tmp1,tmp2 = p1.next,prev.next
            p1.next=prev
            prev.next=tmp1
            p1,prev=tmp1,tmp2
        return head
        
        
