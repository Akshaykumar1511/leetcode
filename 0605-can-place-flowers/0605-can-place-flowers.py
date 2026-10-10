class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            le=(i==0) or (flowerbed[i-1]==0)
            re=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            if flowerbed[i]==0 and le and re:
                flowerbed[i]=1
                n-=1
            if n<=0:
                return True
        return n<=0