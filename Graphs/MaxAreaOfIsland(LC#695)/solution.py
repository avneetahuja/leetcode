class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        def search(i,j):
            grid[i][j] = -1
            l,r,u,d = 0,0,0,0
            if j+1<len(grid[0]) and grid[i][j+1]==1:
                r = search(i,j+1)
            if i+1<len(grid) and grid[i+1][j]==1:
                d = search(i+1,j)
            if j-1>=0 and grid[i][j-1]==1:
                l = search(i,j-1)
            if i-1>=0 and grid[i-1][j]==1:
                u = search(i-1,j)
            return 1+l+r+u+d
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    maxA = max(maxA,search(i,j))
        return maxA
