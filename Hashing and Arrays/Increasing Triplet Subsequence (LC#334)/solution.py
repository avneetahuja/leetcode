class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        A,B = nums[0],float('inf')
        for n in nums:
            if n < A:
                A = n
            if n > A:
                B = min(B,n)
            if n > B:
                return True
        return False
