class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        pair = [[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        for i in pair:
            time = (target-i[0])/i[1]
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
