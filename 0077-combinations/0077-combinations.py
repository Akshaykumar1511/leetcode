class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start):
            if len(sol)==k:
                res.append(sol[:])
                return
            for i in range(start,n+1):
                sol.append(i)
                backtrack(i+1)
                sol.pop()
        
        sol,res=[],[]
        backtrack(1)
        return res