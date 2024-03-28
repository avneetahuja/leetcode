class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res =[]
        pac = set()
        atl = set()
        R,C = len(heights),len(heights[0])
        def search(i,j,visit,prevH):
            if ((i,j) in visit or i<0 or j<0 or i==R or j==C or heights[i][j]<prevH):
                return
            visit.add((i,j))
            search(i+1,j,visit,heights[i][j])
            search(i,j+1,visit,heights[i][j])
            search(i-1,j,visit,heights[i][j])
            search(i,j-1,visit,heights[i][j])
        for c in range(C):
            search(0,c,pac,heights[0][c])
            search(R-1,c,atl,heights[R-1][c])
        for r in range(R):
            search(r,0,pac,heights[r][0])
            search(r,C-1,atl,heights[r][C-1])
        for i in range(R):
            for j in range(C):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
