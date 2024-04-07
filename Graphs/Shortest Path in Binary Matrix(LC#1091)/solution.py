from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        start = (0,0)
        seen = {start: True}
        q = deque()
        q.append(start)
        directions = [(0,1),(1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,-1),(-1,0)]
        while q:
            x,y = q.popleft()
            distance = grid[x][y]
            if x==n-1 and y == n-1:
                return distance+1
            else:
                for dx,dy in directions:
                    newX = x+dx
                    newY = y+dy
                    if 0<=newX<n and 0<=newY<n and grid[newX][newY]==0 and not (newX,newY) in seen:
                        q.append((newX,newY))
                        seen[(newX,newY)] = True
                        grid[newX][newY] = distance+1
                
        return -1
