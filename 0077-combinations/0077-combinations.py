class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol,res=[],[]
        def back(st):
            if len(res)==k:
                sol.append(res[:])
                return
            for i in range(st,n+1):
                res.append(i)
                back(i+1)
                res.pop()
        back(1)
        return sol
        