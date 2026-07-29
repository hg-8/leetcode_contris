# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Compute length of list A
        n = self.findlength(headA)
        
        # Compute length of list B
        m = self.findlength(headB)
        
        # Set pointer fp to head of list A
        fp = headA
        
        # Set pointer sp to head of list B
        sp = headB
        
        # Equalize starting positions by advancing pointer of longer list by length difference
        if m <= n:
            for i in range(n - m):
                fp = fp.next  # Advance fp if list A is longer or equal
        else:
            for i in range(m - n):
                sp = sp.next  # Advance sp if list B is longer
                
        # Traverse both lists synchronously node by node
        while fp is not None:
            # If pointers match, intersection node is found
            if fp == sp:
                return fp
            fp = fp.next
            sp = sp.next
            
        # If traversal reaches end without match, lists do not intersect
        return None
    
    # Helper function to count the number of nodes in a linked list
    def findlength(self, head):
        length = 0
        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1
        return length