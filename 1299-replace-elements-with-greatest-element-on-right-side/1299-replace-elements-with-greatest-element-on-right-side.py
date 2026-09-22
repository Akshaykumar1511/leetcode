class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # if len(arr)==1:
        #     return [-1]
        # else:
        #     res=[-1]*len(arr)
        #     for i in range(len(arr)-1):
        #         j=i+1
        #         highest=-1
        #         while j<len(arr):
        #             highest=max(highest,arr[j])
        #             j+=1
        #         res[i]=highest
        # return res

        maxs=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=maxs
            if curr>maxs:
                maxs=curr
        return arr