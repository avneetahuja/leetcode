class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack =[]
        answer = [-1] * len(nums)
        copy = nums+nums
        for i,n in enumerate(copy):
            while stack and n>stack[-1][0]:
                _,index = stack.pop()
                if index<len(nums):
                    answer[index] = n
            stack.append([n,i])
        return answer
