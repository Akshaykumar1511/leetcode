# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cnt=0
        # curr=head
        # while curr:
        #     curr=curr.next
        #     cnt+=1
        # if cnt==n:
        #     return head.next
        # curr=head
        # for i in range(cnt-n-1):
        #     curr=curr.next
        # curr.next=curr.next.next
        # return head
        dummy=ListNode()
        dummy.next=head
        ahead,behind=dummy,dummy
        for i in range(n+1):
            ahead=ahead.next
        while ahead:
            behind=behind.next
            ahead=ahead.next
        behind.next=behind.next.next
        return dummy.next