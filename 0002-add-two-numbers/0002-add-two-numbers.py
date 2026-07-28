class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 1. Fake/placeholder node
        curr = dummy         # 2. Pointer starts at dummy
        carry = 0
        
        while l1 or l2 or carry:  # 3. Loop handles everything!
            val1 = l1.val if l1 else 0  # 4. Safely get val1
            val2 = l2.val if l2 else 0  # 5. Safely get val2
            
            total = val1 + val2 + carry  # 6. Calculate total sum
            carry = total // 10          # 7. Get new carry
            
            curr.next = ListNode(total % 10)  # 8. Create node directly
            curr = curr.next                  # 9. Move pointer
            
            if l1: l1 = l1.next  # 10. Advance l1 if it exists
            if l2: l2 = l2.next  # 11. Advance l2 if it exists
            
        return dummy.next  # 12. Return actual head!