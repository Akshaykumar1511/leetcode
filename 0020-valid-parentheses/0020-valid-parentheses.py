class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i==")":
                if not a or a[-1]!="(":
                    return False
                else:
                    a.pop()
            elif i=="}":
                if not a or a[-1]!="{":
                    return False
                else:
                    a.pop()
            elif i=="]":
                if not a or a[-1]!="[":
                    return False
                else:
                    a.pop()
            else:
                a.append(i)
        if not a:
            return True
        else:
            return False