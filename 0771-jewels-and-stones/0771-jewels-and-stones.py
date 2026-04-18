class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt=0
        jewel=set(jewels)
        for i in stones:
            if i in jewel:
                cnt+=1
        return cnt