class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countera={}
        counterb={}
        for i in s:
            if i not in countera:
                countera[i]=1
            else:
                countera[i]+=1
        for i in t:
            if i not in counterb:
                counterb[i]=1
            else:
                counterb[i]+=1

        if countera==counterb:
            return True
        else:
            return False