from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def back(node):
            state=states[node]
            if state==visited: return True
            elif state==visiting: return False
            states[node]=visiting
            for nei in d[node]:
                if not back(nei):
                    return False
            if node not in s: s.append(node)
            states[node]=visited
            return True
        visited=2
        visiting=1
        unvisited=0
        states=[unvisited]*numCourses
        s=[]
        d=defaultdict(list)
        for i,v in prerequisites:
            d[i].append(v)
        for node in range(numCourses):
            if not back(node):
                return []
        return s