from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=Counter(stones)
        cnt=0
        for i,j in count.items():
            if i in jewels:
                cnt+=j
        return cnt