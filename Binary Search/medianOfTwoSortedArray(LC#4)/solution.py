class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return median(sorted(nums1+nums2)) # WOW beat 88.28% runtime
        total=len(nums1)+len(nums2)
        half = total//2
        lSmall,rSmall,lBig,rBig,small,big=0,len(nums1)-1,0,len(nums2)-1,nums1,nums2
        if len(nums2)<len(nums1):
            rBig,rSmall,big,small=len(nums1)-1,len(nums2)-1,nums1,nums2
        while True:
            mSmall = lSmall + (rSmall-lSmall)//2
            mBig = half-mSmall-2
            Aleft = small[mSmall] if mSmall >= 0 else float("-infinity")
            Aright = small[mSmall + 1] if (mSmall + 1) < len(small) else float("infinity")
            Bleft = big[mBig] if mBig >= 0 else float("-infinity")
            Bright = big[mBig + 1] if (mBig + 1) < len(big) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                rSmall = mSmall - 1
            else:
                lSmall = mSmall + 1
