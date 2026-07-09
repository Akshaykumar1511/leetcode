class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le=len(numbers)
        l,r=0,le-1
        while l<r:
            if (numbers[l]+numbers[r])>target:
                r-=1
            elif (numbers[l]+numbers[r])<target:
                l+=1
            else:
                return [l+1,r+1]