class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=""
        for i in s:
            if i.isalnum():
                ch+=i.lower()
        
        left,right=0,len(ch)-1
        while left<right:
            if ch[left]!=ch[right]:
                return False
            left+=1
            right-=1
        return True