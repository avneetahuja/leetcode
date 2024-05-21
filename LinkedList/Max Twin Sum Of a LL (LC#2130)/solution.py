# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val+head.next.val
        slow, fast = head, head.next
        sums = [slow.val]
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            sums.append(slow.val)
        # print(sums)
        slow = slow.next
        i = len(sums)-1
        while slow:
            sums[i]+=slow.val
            i-=1
            slow = slow.next
        # print(sums)
        return max(sums)
        
