class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,v in enumerate(s):
            res+=((26-(ord(v)-97))*(i+1))
        return res
        