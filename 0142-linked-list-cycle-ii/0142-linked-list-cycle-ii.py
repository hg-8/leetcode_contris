# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow pointer at head
        slow = head
        
        # Initialize fast pointer at head
        fast = head
        
        # Variable to store intersection node inside cycle
        inspoint = None
        
        # Phase 1: Detect cycle using Floyd's Tortoise and Hare algorithm
        while True:
            # If fast reaches end of list, no cycle exists; return None
            if fast is None or fast.next is None:
                return None
                
            # Move fast 2 steps ahead
            fast = fast.next.next
            
            # Move slow 1 step ahead
            slow = slow.next
            
            # If slow and fast meet, cycle is confirmed; record meeting point and exit loop
            if slow == fast:
                inspoint = slow
                break
                
        # Phase 2: Find cycle entry node by moving head pointer and meeting point pointer at 1 step/iter
        start = head
        while start != inspoint:
            start = start.next
            inspoint = inspoint.next
            
        # Both pointers meet at entry node of the cycle; return entry node
        return start