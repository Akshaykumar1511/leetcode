from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a={}
        for i in text:
            if i in a:
                a[i]=a[i]+1
            else:
                a[i]=1
        return min(
            a.get("b",0),
            a.get("a",0),
            a.get("l",0)//2,
            a.get("o",0)//2,
            a.get("n",0)
        )