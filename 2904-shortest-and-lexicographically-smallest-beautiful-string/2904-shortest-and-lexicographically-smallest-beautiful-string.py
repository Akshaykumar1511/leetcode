class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        d={'0':0,'1':0}
        j=0
        n=len(s)
        ans=float('inf')
        ret=""
        for i in range(n):
            d[s[i]]=d[s[i]]+1
            while d['1']>=k:
                if ans>i-j+1:
                    ans=min(ans,i-j+1)
                    ret=s[j:i+1]
                elif ans==i-j+1 and s[j:i+1]<ret:
                    ret=s[j:i+1]
                d[s[j]]-=1
                j+=1
        return ret
