class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #columns
        for i in range(9):
            a=set()
            for j in range(9):
                if board[i][j] in a:
                    return False
                elif board[i][j] != ".":
                    a.add(board[i][j])

        #rows
        for i in range(9):
            a=set()
            for j in range(9):
                if board[j][i] in a:
                    return False
                elif board[j][i] != ".":
                    a.add(board[j][i])
        #each grid
        starts={(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)}
        for i,j in starts:
            a=set()
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if board[k][l] in a:
                        return False
                    elif board[k][l] != ".":
                        a.add(board[k][l])
        return True