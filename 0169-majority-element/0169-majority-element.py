from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # my own solution
        # a=Counter(nums)
        # ln=len(nums)/2
        # most_rep=a.most_common(1)
        # if most_rep[0][1]>ln:
        #     return most_rep[0][0]

        #brute force
        # a=Counter(nums)
        # ln=len(nums)/2
        # mostrep=-1
        # ans=-1
        # for k,v in a.items():
        #     if v>mostrep:
        #         mostrep=v
        #         ans=k
        # if mostrep>ln:
        #     return ans

        ans=-1
        cnt=0
        for i in nums:
            if cnt==0:
                ans=i
                cnt+=1
            elif i==ans:
                cnt+=1
            else:
                cnt-=1
        return ans