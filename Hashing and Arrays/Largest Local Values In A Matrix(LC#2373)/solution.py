class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        answer = [[-1 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                local_max=-1
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        local_max = max(local_max,grid[k][l])
                answer[i][j] = local_max
        return answer
       
