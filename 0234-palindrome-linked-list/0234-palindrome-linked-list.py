# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n=self.findlength(head)
        if n==1:
            return True
        reversepoint=n//2
        if (n%2 == 1):
            reversepoint = n//2 +1
        head2=self.findloc(head,reversepoint)
        prev=self.findloc(head,reversepoint-1)
        self.reverse(head2,prev)
        first= head
        second=prev.next
        while first is not None and second is not None:
            if (first.val != second.val):
                return False
            first = first.next
            second = second.next
        return True

    def findloc(self,head,pos):
        count=0
        curr=head
        while (count<pos):
            count+=1
            curr=curr.next
        return curr

    def findlength(self,head):
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        return length
    def reverse(self,head,prev):
        f=head
        s=head.next
        while f is not None and s is not None:
            temp=s.next
            s.next=f
            f=s
            s=temp
        head.next=None
        prev.next=f
        
