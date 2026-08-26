class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        a=s.split()
        a=a[-1]
        return len(a)
