from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        def backtrack(start):
            if sum(sol)==target:
                res.append(sol[:])
                return
            if sum(sol)>target:
                return
            for i in range(start,len(candidates)):
                sol.append(candidates[i])
                backtrack(i)
                sol.pop()
        backtrack(0)
        return res