class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        count = 0

        def search(i,j):
            if (i,j) in visited:
                return
            visited[(i,j)] = True
            if j+1<len(grid[0]) and grid[i][j+1]=="1":
                search(i,j+1)
            if i+1<len(grid) and grid[i+1][j]=="1":
                search(i+1,j)
            if j-1>=0 and grid[i][j-1]=="1":
                search(i,j-1)
            if i-1>=0 and grid[i-1][j]=="1":
                search(i-1,j)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0" or (i,j) in visited:
                    continue
                else:
                    count+=1
                    search(i,j)
        return count
        
