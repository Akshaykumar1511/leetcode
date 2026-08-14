class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s,r=[],[]
        n=len(nums)
        def backtrack(i):
            if i==n:
                r.append(s[:])
                return
            
            backtrack(i+1)

            s.append(nums[i])
            backtrack(i+1)
            s.pop()
        backtrack(0)
        return r