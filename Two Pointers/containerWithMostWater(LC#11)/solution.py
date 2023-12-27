class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2,maxA = 0,len(height)-1,0
        while p1<p2:
            maxA = max(maxA,min(height[p1],height[p2])*(p2-p1))
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return maxA
