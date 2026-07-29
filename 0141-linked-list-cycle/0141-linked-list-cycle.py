# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Finding Algorithm (Tortoise and Hare)
        # Slow pointer advances 1 node per step
        slow = head
        
        # Fast pointer advances 2 nodes per step
        fast = head
        
        # Traverse list safely as long as fast pointer and fast.next are valid (non-null)
        while fast is not None and fast.next is not None:
            # Advance slow pointer by 1 step
            slow = slow.next
            
            # Advance fast pointer by 2 steps
            fast = fast.next.next
            
            # If slow and fast pointers meet, a loop/cycle is detected in the list
            if slow == fast:
                return True
                
        # If fast pointer hits end of list (None), no cycle exists
        return False