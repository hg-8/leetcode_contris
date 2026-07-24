# Definition for singly-linked list.
# class List:
#     def __init__(self,val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[List], list2: Optional[List]
    ) -> Optional[List]:
        p1 = list1
        p2 = list2
        head = None
        tail = None
        while p1 is not None or p2 is not None:
            val = None
            if p1 is not None and p2 is not None:
                if p1.val >= p2.val:
                    val = p2.val
                    p2 = p2.next
                else:
                    val = p1.val
                    p1 = p1.next
            elif p1 is not None:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next
            if tail is None:
                head = self.insertAtend(tail, val)
                tail = head
            else:
                tail = self.insertAtend(tail, val)
        return head

    def insertAtend(self, tail, val):
        nn = ListNode(val)
        if tail is not None:
            tail.next = nn
        return nn
