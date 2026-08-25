"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited=set()
        start=node
        stk=[node]
        o_to_n={}
        visited.add(start)
        while stk:
            curnode=stk.pop()
            o_to_n[curnode]=Node(val=curnode.val)
            for nei in curnode.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        
        for old_node,new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(o_to_n[nei])
        return o_to_n[start]