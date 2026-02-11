class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resa,resb=[0]*26,[0]*26
        for i in s:
            a=ord(i)-97
            resa[a]+=1
        for i in t:
            a=ord(i)-97
            resb[a]+=1
        if resa==resb:
            return True
        else:
            return False