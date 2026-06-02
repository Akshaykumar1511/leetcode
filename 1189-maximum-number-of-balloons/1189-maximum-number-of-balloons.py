from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a={}
        for i in text:
            if i in a:
                a[i]=a[i]+1
            else:
                a[i]=1
        b={"a","b","l","o","n"}
        if all(ch in a for ch in "ballon"):
            return min(a["b"],a["a"],a["l"]//2,a["o"]//2,a["n"])
        else:
            return 0