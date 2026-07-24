# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n=self.findlength(headA)
        m=self.findlength(headB)
        fp=headA
        sp=headB
        if (m <= n):
            for i in range(n-m):
                fp=fp.next
        else:
            for i in range(m-n):
                sp=sp.next
        while fp is not None:
            if(fp==sp):
                return fp
            fp=fp.next
            sp=sp.next
        return None
    
    def findlength(self,head):
        length=0
        curr=head
        while curr.next is not None:
            curr=curr.next
            length+=1
        return length
        


        