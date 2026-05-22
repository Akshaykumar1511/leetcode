class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter=defaultdict(int)
        ballon='balloon'
        for i in text:
            counter[i]+=1
        if any(c not in counter for c in ballon):
            return 0
        else:
            return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])