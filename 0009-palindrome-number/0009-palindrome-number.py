class Solution:
    def isPalindrome(self, x: int) -> bool:
        ch=str(x)
        left,right=0,len(ch)-1
        while left<right:
            if ch[left]!=ch[right]:
                return False
            left+=1
            right-=1
        return True
            