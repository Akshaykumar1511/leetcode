from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def back(node):
            state=states[node]
            if state==visited: return True
            elif state==visiting: return False
            states[node]=visiting
            for nei in d[node]:
                if not back(nei):
                    return False
            states[node]=visited
            return True
            
        visited=2
        unvisited=0
        visiting=1
        d=defaultdict(list)
        states=[unvisited]*numCourses
        for i,v in prerequisites:
            d[i].append(v)
        for i in range(numCourses):
            if not back(i):
                return False
        return True