class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        if (n==1 and m==1) and board[n-1][m-1]==word:
            return True
        ln=len(word)
        def backtrack(pos,index):
            i,j=pos
            if index==ln:
                return True
            if board[i][j]!=word[index]:
                return False
            char=board[i][j]
            board[i][j]="#"
            for i_off,j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                r,c=i+i_off,j+j_off
                if 0<=r<n and 0<=c<m:
                    if backtrack((r,c),index+1):
                        return True
            board[i][j]=char
            return False

        for i in range(n):
            for j in range(m):
                if backtrack((i,j),0):
                    return True
        return False