class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            conditions to follow: 
            1) n = open = close
            2) close < open (when generating)
            3) open < n, basically add as many open you want but close can only be added when number of existing open is more
        '''
        stack = []
        ans = []

        def generate(openCount,closeCount):
            if openCount == closeCount == n:
                ans.append("".join(stack))
            
            if closeCount<openCount:
                stack.append(")")
                generate(openCount,closeCount+1)
                stack.pop()
            
            if openCount<n:
                stack.append("(")
                generate(openCount+1,closeCount)
                stack.pop()
        
        generate(0,0)
        return ans
