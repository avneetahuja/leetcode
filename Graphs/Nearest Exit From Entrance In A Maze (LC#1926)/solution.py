from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R,C = len(maze),len(maze[0])
        queue = collections.deque()
        queue.append((entrance[0],entrance[1],0))
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = {}
        while queue:
            x,y,step = queue.popleft()
            
            if (x,y) in visited:
                continue
            elif (x==0 or y==0 or x==R-1 or y==C-1) and step>0:
                return step
            else:
                visited[(x,y)] = True
                for dx,dy in dirs:
                    i = x+dx
                    j = y+dy
                    if 0<=i<R and 0<=j<C and maze[i][j]=='.':
                        queue.append([i,j,step+1])
        return -1
