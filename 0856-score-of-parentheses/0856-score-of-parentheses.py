class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]  # Base layer score

        for char in s:
            if char == "(":
                stk.append(0)
            else:
                v = stk.pop()
                stk[-1] += max(2 * v, 1)

        return stk[0]