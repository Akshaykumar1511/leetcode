from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        d=defaultdict(list)
        for i,u in edges:
            d[i].append(u)
            d[u].append(i)
        seen=set()
        seen.add(source)
        def rec(i):
            if destination==i:
                return True
            for j in d[i]:
                if j not in seen:
                    seen.add(j)
                    if rec(j):
                        return True
            return False
        return rec(source)