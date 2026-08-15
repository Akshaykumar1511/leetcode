from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination: return True
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        seen=set()
        seen.add(source)
        def back(i):
            if i == destination:
                return True
            for node in d[i]:
                if node not in seen:
                    seen.add(node)
                    if back(node):
                        return True
            return False
        return back(source)