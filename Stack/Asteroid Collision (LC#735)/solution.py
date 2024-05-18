class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            elif a < 0:
                flag =True
                while stack and stack[-1]>0:
                    top = stack.pop()
                    res = a/top
                    if res < -1:
                        continue
                        # stack.append(a)
                    elif res == -1:
                        flag=False
                        break
                    else:
                        flag = False
                        stack.append(top)
                        break
                if flag:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
                
