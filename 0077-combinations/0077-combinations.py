class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(st):
            if len(s)==k:
                r.append(s[:])
                return
            for i in range(st,n+1):
                s.append(i)
                backtrack(i+1)
                s.pop()
        s,r=[],[]
        backtrack(1)
        return r