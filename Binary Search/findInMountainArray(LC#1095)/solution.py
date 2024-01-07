# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        minIndex=-1
        l,r,peak=0,mountain_arr.length()-1,-1
        while l<=r:
            m=l+(r-l)//2
            
            if 0<m<mountain_arr.length()-1:
                L=mountain_arr.get(m-1)
                R=mountain_arr.get(m+1)
                M=mountain_arr.get(m)
                if M>L and M>R:
                    peak=m
                    break
                elif M<R:
                    l=m+1
                else: 
                    r=m-1
            elif m==0:
                peak=m+1
                break
            else:
                peak=m-1
                break
        l1,r1,l2,r2=0,peak,peak,mountain_arr.length()-1
        while l1<=r1:
            m=l1+(r1-l1)//2
            M=mountain_arr.get(m)
            if M==target:
                return m
            elif M<target:
                l1=m+1
            else:
                r1=m-1
        while l2<=r2:
            m=l2+(r2-l2)//2
            M=mountain_arr.get(m)
            if M==target:
                return m
            elif M<target:
                r2=m-1
            else:
                l2=m+1
        return minIndex
        
