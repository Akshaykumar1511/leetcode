# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode()
        curr=dum
        carry=0
        while l1 or l2 or carry:
            l1v=l1.val if l1 else 0
            l2v=l2.val if l2 else 0
            summ=l1v+l2v+carry
            carry=summ//10
            temp=ListNode(summ%10)
            curr.next=temp
            curr=temp
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dum.next