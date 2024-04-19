class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l,r = 0,0
        while l<n:
            if nums[l] == 0:
                r=l+1
                while r<n and nums[r]==0:
                    r+=1
                if r>=n:
                    break
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
            l+=1
