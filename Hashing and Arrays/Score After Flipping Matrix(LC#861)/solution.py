class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        for i in range(R):
            if grid[i][0]==0:
                for j in range(C):
                    if grid[i][j]==0:
                        grid[i][j]=1
                    else:
                        grid[i][j] = 0
        for j in range(1,C):
            count_zero = 0
            count_one = 0
            for i in range(R):
                if grid[i][j]==1:
                    count_one+=1
                else:
                    count_zero+=1
            if count_zero>count_one:
                for i in range(R):
                    if grid[i][j]==0:
                        grid[i][j]=1
                    else:
                        grid[i][j] = 0
        s = 0
        for i in range(R):
            binary_string = ''.join(str(bit) for bit in grid[i])
            s+=int(binary_string, 2)
        return s
