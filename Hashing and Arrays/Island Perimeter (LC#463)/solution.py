class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        R = len(grid)
        C = len(grid[0])
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    if i==0:
                        res+=1
                    if j==0:
                        res+=1
                    if i==R-1:
                        res+=1
                    if j==C-1:
                        res+=1
                    for di,dj in dirs:
                        x = i+di
                        y = j+dj
                        if 0<=x<R and 0<=y<C and grid[x][y]==0:
                            res+=1
        return res
