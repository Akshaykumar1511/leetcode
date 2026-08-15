class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        n=len(digits)
        sol,res=[],[]
        def backtrack(start):
            if len(sol)==n:
                res.append("".join(sol[:]))
                return
            for v in dic[digits[start]]:
                sol.append(v)
                backtrack(start+1)
                sol.pop()
        backtrack(0)
        return res