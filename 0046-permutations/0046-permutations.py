class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s,r=[],[]
        def backtrack():
            if len(nums)==len(s):
                r.append(s[:])
                return
            for i in nums:
                if i not in s:
                    s.append(i)
                    backtrack()
                    s.pop()
        backtrack()
        return r