class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Make prefix and postfix arrays and multiply them through, for the O(1) space complexity, combine the prefix and postfix and end up with the ugly soln below
        '''
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
