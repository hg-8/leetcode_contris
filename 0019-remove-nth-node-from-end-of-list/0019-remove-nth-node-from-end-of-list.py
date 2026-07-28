# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head 
        fast = head
        
        # 1. Advance fast pointer by n steps
        for i in range(n):
            fast = fast.next
            
        # 2. Edge Case: Removing the head node itself
        if fast is None:
            return head.next
            
        # 3. Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        # 4. Remove the N-th node from end
        slow.next = slow.next.next
        
        return head


            
            
            