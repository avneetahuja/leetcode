class Solution:
    def trap(self, height: List[int]) -> int:
        p1,p2,totalWater = 0,len(height)-1,0
        lmax,rmax = height[p1],height[p2]
        while p1<p2:
            if lmax<rmax:
                p1+=1
                lmax = max(lmax,height[p1])
                totalWater+=lmax - height[p1]
            else:
                p2-=1
                rmax = max(rmax,height[p2])
                totalWater += rmax - height[p2]
        return totalWater
