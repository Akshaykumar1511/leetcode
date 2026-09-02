class Solution:
    def isHappy(self, n: int) -> bool:
        #tried error
        # num=n
        # while len(str(num))!=1:
        #     temp=0
        #     for i in str(num):
        #         temp+=int(i)**2
        #     num=int(temp)
        # if num==1:
        #     return True
        # else:
        #     return False

        
        # Keep going as long as we haven't reached 1, 
        # AND we haven't fallen into a repeating cycle.
        seen=set()
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Your exact logic for summing the squares
            temp = 0
            for i in str(n):
                temp += int(i) ** 2
            n = temp
            
        # If the loop broke because n became 1, it's happy.
        # If it broke because n was in 'seen', it's unhappy.
        return n == 1