from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1 using heap time complexity=O(nlogk)
        # counter=Counter(nums)
        # heap=[]
        # for key,val in counter.items():
        #     if len(heap)<k:
        #         heapq.heappush(heap,(val,key))
        #     else:
        #         heapq.heappushpop(heap,(val,key))
        # return [i[1] for i in heap]

        #method 2 using list only time complexity=O(n)
        counter=Counter(nums)
        ln=len(nums)
        n=[0]*(ln+1)
        for i,v in counter.items():
            if n[v]!=0:
                n[v].append(i)
            else:
                n[v]=[i]
        ans=[]
        for i in range(ln,-1,-1):
            if n[i]!=0:
                ans.extend(n[i])
            if len(ans)==k:
                break
        return ans