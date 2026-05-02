class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sjew=set(jewels)
        cnt=0
        for i in stones:
            if i in sjew:
                cnt+=1
        return cnt