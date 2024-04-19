class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        C = len(grid[0])
        R = len(grid)

        def search(i,j):
            for dx,dy in dirs:
                x = i+dx
                y = j+dy
                if 0<=x<R and 0<=y<C and grid[x][y]=="1":
                    grid[x][y]='#'
                    search(x,y)

        for i in range(R):
            for j in range(C):
                if grid[i][j]=="1":
                    grid[i][j]='#'
                    search(i,j)
                    count+=1
        
        return count
