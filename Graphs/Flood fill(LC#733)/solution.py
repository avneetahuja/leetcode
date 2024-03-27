class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        def search(i,j,startColor):
            image[i][j] = color
            if j+1<len(image[0]) and image[i][j+1]==startColor:
                search(i,j+1,startColor)
            if i+1<len(image) and image[i+1][j]==startColor:
                search(i+1,j,startColor)
            if j-1>=0 and image[i][j-1]==startColor:
                search(i,j-1,startColor)
            if i-1>=0 and image[i-1][j]==startColor:
                search(i-1,j,startColor)
        search(sr,sc,image[sr][sc])
        return image
