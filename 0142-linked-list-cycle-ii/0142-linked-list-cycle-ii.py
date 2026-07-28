# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        inspoint=None
        while True:
            if fast is None or fast.next is None:
                return None
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                inspoint=slow
                break
        start=head
        while start!=inspoint:
            start=start.next
            inspoint=inspoint.next
        return start