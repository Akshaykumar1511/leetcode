class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res=[]
        for i in asteroids:
            while res and i<0 and res[-1]>0:
                diff=i+res[-1]
                if diff>0:
                    i=0
                elif diff<0:
                    res.pop()
                else:
                    i=0
                    res.pop()
            if i:
                res.append(i)
        return res