class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):        
            while stack and t>stack[-1][0]:
                answer[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append([t,i])
        return answer
