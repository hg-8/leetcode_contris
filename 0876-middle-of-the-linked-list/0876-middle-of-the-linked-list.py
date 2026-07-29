# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast & Slow Pointer Strategy (Floyd's Algorithm variant)
        # Initialize slow pointer at head (moves 1 step at a time)
        # Initialize fast pointer at head (moves 2 steps at a time)
        slow, fast = head, head
        
        # Traverse list until fast pointer or fast.next reaches end (None)
        while fast and fast.next:
            # Advance slow pointer 1 node ahead
            slow = slow.next
            
            # Advance fast pointer 2 nodes ahead
            fast = fast.next.next
            
        # When fast reaches end, slow points exactly at the middle node of the list
        return slow