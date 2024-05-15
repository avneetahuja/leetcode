class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lSum = [0] * n
        rSum = [0] * n
        for i in range(1,n):
            lSum[i] = lSum[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            rSum[i] = rSum[i+1] + nums[i+1]
        for i in range(n):
            if lSum[i]==rSum[i]:
                return i
        return -1
        
