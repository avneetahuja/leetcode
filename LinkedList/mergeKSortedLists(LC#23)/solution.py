# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            merged = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = None if (i+1) >=len(lists) else lists[i+1]
                merged.append(self.merge(l1,l2))
            lists=merged
        
        return lists[0]
    def merge(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        if list1.val<list2.val:
            head = list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        curr=head
        while list1 or list2:
            if not list1:
                curr.next=list2
                curr=curr.next
                list2=list2.next
            elif not list2:
                curr.next=list1
                curr=curr.next
                list1=list1.next
            elif list1.val<list2.val:
                curr.next=list1
                curr=curr.next
                list1=list1.next
            else:
                curr.next=list2
                curr=curr.next
                list2=list2.next
        return head
        
