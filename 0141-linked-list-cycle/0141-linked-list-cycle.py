# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Traverse as long as the fast pointer and its next node exist
        while fast is not None and fast.next is not None:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps
            
            # If slow and fast pointers meet at the same node, a cycle exists
            if slow == fast:
                return True
                
        # If fast reaches None, there is no cycle
        return False