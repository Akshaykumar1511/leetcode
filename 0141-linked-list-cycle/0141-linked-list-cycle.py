# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr=head
        # a=set()
        # while curr:
        #     if curr in a:
        #         return True
                
        #     a.add(curr)
        #     curr=curr.next
        # return False
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False