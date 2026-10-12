class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a', 'e', 'i', 'o', 'u'}
        vc=sum(1 for i in range(k) if s[i] in vowels)
        bs=vc
        for i in range(len(s)-k):
            if s[i] in vowels:
                vc-=1
            if s[i+k] in vowels:
                vc+=1
            bs=max(bs,vc)
        return bs