class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        R = len(land)
        C = len(land[0])
        
        def searchRD(i,j):
            x1,y1,x2,y2 = i,j,i,j
            if 0<=x1+1<R and land[x1+1][y1]==1:
                land[x1+1][y1] = -1
                x1,y1 = searchRD(x1+1,y1)
            if 0<=y2+1<C and land[x2][y2+1]==1:
                land[x2][y2+1]=-1
                x2,y2 = searchRD(x2,y2+1)
            return [max(x1,x2),max(y1,y2)]


        for i in range(R):
            for j in range(C):
                if land[i][j]==1:
                    land[i][j]=-1
                    cur = [i,j]
                    cur += searchRD(i,j)
                    res.append(cur)
        return res
