# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy=ListNode(0,head)
        lp=dummy
        curr=head
        for _ in range(left-1):
            curr=curr.next
            lp=lp.next
        pp=None
        for _ in range(right-left+1):
            np=curr.next
            curr.next=pp
            pp=curr
            curr=np
        temp=lp.next
        temp.next=curr
        lp.next=pp
        return dummy.next