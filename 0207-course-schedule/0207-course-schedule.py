from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def back(i):
            state=states[i]
            if state==visited:
                return True
            elif state==visiting:
                return False
            states[i]=visiting
            for pre in d[i]:
                if not back(pre):
                    return False
            states[i]=visited
            return True
        d=defaultdict(list)
        for i,v in prerequisites:
            d[i].append(v)
        visited=2
        visiting=1
        unvisited=0
        states=[0]*numCourses
        for i in range(numCourses):
            if not back(i):
                return False
        return True
        