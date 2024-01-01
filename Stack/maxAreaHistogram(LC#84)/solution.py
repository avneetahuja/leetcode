class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        maxArea=0
        for i,h in enumerate(heights):
            start = i
            while(stack and stack[-1][1]>h):
                start,height = stack.pop()
                maxArea = max(maxArea, height*(i-start))
            stack.append([start,h])
        
        for s in stack:
            maxArea = max(maxArea, s[1] * (len(heights)-s[0]))
        return maxArea
