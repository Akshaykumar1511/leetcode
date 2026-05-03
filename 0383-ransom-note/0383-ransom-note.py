class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                pos=magazine.index(i)
                magazine=magazine[:pos]+magazine[pos+1:]
            else:
                return False
        return True