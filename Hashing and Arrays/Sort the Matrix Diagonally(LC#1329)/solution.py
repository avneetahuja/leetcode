class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        for r in range(R):
            i,j = r,0
            arr = []
            while i<R and j<C:
                # print(i,j)
                arr.append(mat[i][j])
                i+=1
                j+=1
            arr.sort()
            i,j = r,0
            while i<R and j<C:
                mat[i][j] = arr[j]
                i+=1
                j+=1
        for c in range(1,C):
            i,j = 0,c
            arr = []
            while i<R and j<C:
                # print(i,j)
                arr.append(mat[i][j])
                i+=1
                j+=1
            arr.sort()
            i,j = 0,c
            while i<R and j<C:
                mat[i][j] = arr[i]
                i+=1
                j+=1
        return mat
            
