# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle of the linked list using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next          # Move slow pointer 1 step
            fast = fast.next.next     # Move fast pointer 2 steps
        
        # Step 2: Reverse the second half of the linked list starting from 'slow' pointer
        prev = None
        curr = slow
        while curr:
            nxt = curr.next           # Save next node
            curr.next = prev          # Reverse pointer direction
            prev = curr               # Advance prev pointer
            curr = nxt                # Advance curr pointer
        
        # Step 3: Compare node values of first half and reversed second half
        first, second = head, prev
        while second:                 # Traverse until end of second half
            if first.val != second.val:
                return False          # Values mismatch -> not a palindrome
            first = first.next
            second = second.next
            
        # All values matched -> linked list is a palindrome
        return True
