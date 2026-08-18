class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join(map(str,digits)))
        a+=1
        a=list(map(int,str(a)))
        return a