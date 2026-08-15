class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest=float('-inf')
        for i in range(len(accounts)):
            summ=0
            for j in range(len(accounts[0])):
                summ+=accounts[i][j]
            highest=max(highest,summ)
        return highest