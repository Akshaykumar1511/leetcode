"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        otn={}
        while curr:
            a=Node(curr.val)
            otn[curr]=a
            curr=curr.next
        curr=head
        while curr:
            a=otn[curr]
            a.next=otn[curr.next] if curr.next else None
            a.random=otn[curr.random] if curr.random else None
            curr=curr.next
        return otn[head]