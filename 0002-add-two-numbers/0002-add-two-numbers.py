class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify linked list construction and avoid edge case handling for head node
        dummy = ListNode(0)
        
        # Pointer 'curr' keeps track of the current tail node in the result linked list
        curr = dummy
        
        # Variable to keep track of digit addition overflow (carry-over to next place value)
        carry = 0
        
        # Continue processing as long as there are nodes remaining in l1 or l2, or a remaining carry to append
        while l1 or l2 or carry:
            # Safely extract digit value from l1 if node exists, otherwise use 0 for missing digits
            val1 = l1.val if l1 else 0
            
            # Safely extract digit value from l2 if node exists, otherwise use 0 for missing digits
            val2 = l2.val if l2 else 0
            
            # Calculate sum of current digits plus carry from the previous lower place value
            total = val1 + val2 + carry
            
            # Compute new carry digit for next higher place value using integer division
            carry = total // 10
            
            # Attach a new node containing the single digit remainder (total % 10) to the result list
            curr.next = ListNode(total % 10)
            
            # Move the pointer to the newly created node
            curr = curr.next
            
            # Advance l1 pointer to next node if l1 is not empty
            if l1: l1 = l1.next
            
            # Advance l2 pointer to next node if l2 is not empty
            if l2: l2 = l2.next
            
        # Return dummy.next which points to the actual head of the resulting linked list
        return dummy.next