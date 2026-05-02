class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols=len(matrix),len(matrix[0])
        left,right,up,down=0,1,2,3
        direction = right
        i,j=0,0
        upwall=0
        downwall=rows
        leftwall=-1
        rightwall=cols
        res=[]

        while rows*cols!=len(res):
            if direction==right:
                while j<rightwall:
                    res.append(matrix[i][j])
                    j+=1
                rightwall-=1
                i+=1
                j-=1
                direction=down
            elif direction==down:
                while i<downwall:
                    res.append(matrix[i][j])
                    i+=1
                downwall-=1
                i-=1
                j-=1
                direction=left
            elif direction==left:
                while j>leftwall:
                    res.append(matrix[i][j])
                    j-=1
                leftwall+=1
                j+=1
                i-=1
                direction=up
            else:
                while i>upwall:
                    res.append(matrix[i][j])
                    i-=1
                upwall+=1
                i+=1
                j+=1
                direction=right
        return res
