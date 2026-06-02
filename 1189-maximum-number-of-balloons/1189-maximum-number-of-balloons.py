from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a=defaultdict(int)
        for i in text:
            if i in a:
                a[i]=a[i]+1
            else:
                a[i]=1
        

        if any(a)==True:
            return min(a["b"],a["a"],a["l"]//2,a["o"]//2,a["n"])
        else:
            return 0