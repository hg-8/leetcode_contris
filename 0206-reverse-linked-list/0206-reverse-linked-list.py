# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize 'prev' pointer to None (will become the tail node of reversed list)
        # Initialize 'curr' pointer at head of original list
        prev, curr = None, head
        
        # Traverse list until current pointer becomes None
        while curr:
            # Save reference to next node before overwriting curr.next pointer
            nxt = curr.next
            
            # Reverse current node's link to point backwards to previous node
            curr.next = prev
            
            # Advance 'prev' pointer to current node
            prev = curr
            
            # Advance 'curr' pointer to next node saved earlier
            curr = nxt
            
        # Return 'prev' pointer which now references the new head of the reversed list
        return prev