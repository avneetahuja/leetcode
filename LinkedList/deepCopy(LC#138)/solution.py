"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            tmp=curr.next
            curr.next=Node(curr.val)
            curr.next.next = tmp
            curr=tmp
        
        # curr=head
        # while curr:
        #     print(curr.val)
        #     curr=curr.next
        # curr=head
        # while curr:
        #     if curr.random:
        #         print(curr.random.val)
        #     curr=curr.next
        # print("CUT")
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr=curr.next.next
        
        # curr=head
        # while curr:
        #     if curr.random:
        #         print(curr.random.val)
        #     curr=curr.next
        
        curr=head
        copy=Node(0)
        zero=copy
        
        while curr:
            front = curr.next.next
            copy.next = curr.next
            curr.next=front
            copy=copy.next
            
            curr=curr.next
        return zero.next
