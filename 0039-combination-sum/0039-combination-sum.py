class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        n=len(candidates)

        # method 1
        # def backtrack(start):
        #     if sum(sol)==target:
        #         res.append(sol[:])
        #         return
        #     if sum(sol)>target:
        #         return
        #     for i in range(start,n):
        #         sol.append(candidates[i])
        #         backtrack(i)
        #         sol.pop()
        # backtrack(0)

        #method 2
        def backtrack(i,cursum):
            if cursum==target:
                res.append(sol[:])
                return
            if cursum>target or i==n:
                return
            
            backtrack(i+1,cursum)

            sol.append(candidates[i])
            backtrack(i,cursum+candidates[i])
            sol.pop()
        backtrack(0,0)
        return res