# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        #iterative
        # dummy,curr=None,head
        # while curr:
        #     nxt=curr.next
        #     curr.next=dummy
        #     dummy=curr
        #     curr=nxt
        # return dummy

        #recursive
        if not head:
            return None
        dumhead=head
        if head.next:
            dumhead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return dumhead