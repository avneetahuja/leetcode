from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        q = collections.deque()
        ones = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    ones+=1
        if ones==0:
            return 0
        if len(q) ==0:
            return -1
        time=0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            length = len(q)
            while length>0:
                i,j = q.popleft()
                length-=1
                for dx,dy in dirs:
                    x,y = i+dx,j+dy
                    if 0<=x<R and 0<=y<C and grid[x][y]==1:
                        grid[x][y]=2
                        ones-=1
                        q.append((x,y))
            time+=1
        if ones==0:
            return time-1
        return -1
