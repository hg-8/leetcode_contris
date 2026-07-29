# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize pointer p1 to traverse list1
        p1 = list1
        
        # Initialize pointer p2 to traverse list2
        p2 = list2
        
        # Track the head node of the merged list (returned at the end)
        head = None
        
        # Track the tail node of the merged list to append new nodes in O(1) time
        tail = None
        
        # Continue loop until all nodes from both lists are processed
        while p1 is not None or p2 is not None:
            val = None
            
            # Case 1: Both lists still have nodes to compare
            if p1 is not None and p2 is not None:
                # Pick the smaller node value to maintain sorted order
                if p1.val >= p2.val:
                    val = p2.val
                    p2 = p2.next  # Advance p2 pointer
                else:
                    val = p1.val
                    p1 = p1.next  # Advance p1 pointer
            # Case 2: Only list1 has remaining nodes
            elif p1 is not None:
                val = p1.val
                p1 = p1.next  # Advance p1 pointer
            # Case 3: Only list2 has remaining nodes
            else:
                val = p2.val
                p2 = p2.next  # Advance p2 pointer
                
            # If merged list is currently empty, initialize head with the first node
            if tail is None:
                head = self.insertAtend(tail, val)
                tail = head  # Set tail to initial head node
            # Otherwise, append node to current tail and update tail pointer
            else:
                tail = self.insertAtend(tail, val)
                
        # Return the head pointer of the merged sorted linked list
        return head

    # Helper method to instantiate a new node and link it after the current tail
    def insertAtend(self, tail, val):
        nn = ListNode(val)  # Create a new ListNode with current value
        if tail is not None:
            tail.next = nn  # Link existing tail to new node
        return nn           # Return new node so caller updates tail reference
