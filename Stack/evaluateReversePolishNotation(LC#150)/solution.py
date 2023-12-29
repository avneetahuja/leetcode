class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans=0
        for t in tokens:
            if t not in ["+","-","*","/"]:
                stack.append(t)
            elif t=="+":
                a =stack.pop()
                b=stack.pop()
                print("+",a,b)
                a = int(a)+int(b)
                stack.append(a)
            elif t=="-":
                a =stack.pop()
                b=stack.pop()
                print("-",a,b)
                a = int(b)-int(a)
                stack.append(a)
            elif t=="*":
                a =stack.pop()
                b=stack.pop()
                print("*",a,b)
                a = int(a)*int(b)
                stack.append(a)
            elif t=="/":
                a =stack.pop()
                b=stack.pop()
                print("/",a,b)
                a = int(b)/int(a)
                a = math.trunc(a)
                stack.append(a)
        return int(stack[0])
