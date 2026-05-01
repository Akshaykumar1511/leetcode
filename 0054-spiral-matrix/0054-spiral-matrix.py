class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        ans=[]
        up,down,left,right=0,1,2,3
        direction=right
        i,j=0,0

        UP_WALL=0
        DOWN_WALL=n
        RIGHT_WALL=m
        LEFT_WALL=-1
        while len(ans)!=n*m:
            if direction==right:
                while j<RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                RIGHT_WALL-=1
                direction=down

            elif direction==down:
                while i<DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                DOWN_WALL-=1
                direction=left

            elif direction==left:
                while j>LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                LEFT_WALL+=1
                direction=up

            else:
                while i>UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                UP_WALL+=1
                direction=right
        return ans