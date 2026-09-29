class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                left_char=s[i+1:j+1]
                right_char=s[i:j]
                return left_char==left_char[::-1] or right_char==right_char[::-1]
            i+=1
            j-=1
        return True