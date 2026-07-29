# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize slow pointer at head to eventually locate node before target
        slow = head 
        
        # Initialize fast pointer at head to create a gap of n nodes relative to slow pointer
        fast = head
        
        # Advance fast pointer by n steps ahead to establish the gap
        for i in range(n):
            fast = fast.next
            
        # Edge Case: If fast became None, n equals list length, meaning head node itself needs removal
        if fast is None:
            # Skip head and return second node as the new head
            return head.next
            
        # Move both pointers at equal speed until fast pointer reaches the last node (fast.next is None)
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        # At this point, slow points right before the target node; bypass target node to delete it
        slow.next = slow.next.next
        
        # Return the modified linked list starting from original head
        return head