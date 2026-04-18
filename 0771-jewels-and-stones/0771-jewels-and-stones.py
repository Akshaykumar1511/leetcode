class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in set(jewels) for s in stones)