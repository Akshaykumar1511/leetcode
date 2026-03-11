class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def joining(n,word1,word2):
            word=""
            for i in range(n):
                word+=(word1[i]+word2[i])
            return word
        w1l=len(word1)
        w2l=len(word2)
        word=""
        if w1l==w2l:
            word=joining(w1l,word1,word2)
        elif w1l<w2l:
            word=joining(w1l,word1,word2)+word2[w1l:]
        else:
            word=joining(w2l,word1,word2)+word1[w2l:]
        return word

            
