class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = {}
        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen[i] = True
        slow,fast=0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        fast=0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            if slow==fast:
                return slow
        
        
        
