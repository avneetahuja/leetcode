class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        maxL = 0
        for n in nSet:
            if (n-1) not in nSet:
                l = 1
                while (n+l) in nSet:
                    l+=1
                maxL = max(maxL,l)
        return maxL
