class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        mx=max(candies)
        rs=[True]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<mx:
                rs[i]=False
            else:
                continue
        return rs