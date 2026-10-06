class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed=0
        add_needed=0
        for i in s:
            if i=="(":
                open_needed+=1
            elif i==")":
                if open_needed>0:
                    open_needed-=1
                else:
                    add_needed+=1
        return open_needed+add_needed