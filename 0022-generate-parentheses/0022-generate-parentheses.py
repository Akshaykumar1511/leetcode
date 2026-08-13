class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        sol,res=[],[]
        def backtrack(op,cl):
            if len(sol)==(2*n) and op==cl:
                res.append("".join(sol[:]))
                return
            if op>cl:
                sol.append(")")
                backtrack(op,cl+1)
                sol.pop()
            if op<n:
                sol.append("(")
                backtrack(op+1,cl)
                sol.pop()
        backtrack(0,0)
        return res