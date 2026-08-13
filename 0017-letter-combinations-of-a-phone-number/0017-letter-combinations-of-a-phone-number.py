class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        sol,res=[],[]
        n=len(digits)
        dic={
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(start):
            if len(sol)==n:
                res.append(sol[:])
                return
            for i in dic[digits[start]]:
                sol.append(i)
                backtrack(start+1)
                sol.pop()
        backtrack(0)
        ret=[]
        for l in res:
            ret.append("".join(l))
        return ret