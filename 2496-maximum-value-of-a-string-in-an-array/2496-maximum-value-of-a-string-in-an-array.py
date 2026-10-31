class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        res=float('-inf')
        for i in strs:
            if i.isdigit():
                res=max(res,int(i))
            else:
                res=max(res,len(i))
        return res