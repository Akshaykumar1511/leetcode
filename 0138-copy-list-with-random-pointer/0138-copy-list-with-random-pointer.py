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
        if not head: return None
        curr=head
        oldtonew={}
        while curr:
            newnode=Node(x=curr.val)
            oldtonew[curr]=newnode
            curr=curr.next
        curr=head
        while curr:
            a=oldtonew[curr]
            a.next=oldtonew[curr.next] if curr.next else None
            a.random=oldtonew[curr.random] if curr.random else None
            curr=curr.next
        return oldtonew[head]