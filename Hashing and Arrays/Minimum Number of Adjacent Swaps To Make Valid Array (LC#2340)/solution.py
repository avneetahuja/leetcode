class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_n = max(nums)
        min_n = min(nums)
        n = len(nums)
        l = r = -1
        for i in range(n-1,-1,-1):
            if nums[i] == max_n:
                r = i
                break
        for i in range(n):
            if nums[i] == min_n:
                l = i
                break
        res = n-1-r+l
        print(l,r)
        if l>r:
            res-=1
        return res
