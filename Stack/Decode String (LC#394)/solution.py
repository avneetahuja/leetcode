class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        for c in s:
            if c == ']':
                string_to_append =""
                while stack[-1]!='[':
                    string_to_append+=stack.pop()
                stack.pop()
                num_string =""
                while stack and stack[-1].isdigit():
                    num_string=stack.pop()+num_string
                for k in range(int(num_string)):
                    for j in range(len(string_to_append)-1,-1,-1):
                        stack.append(string_to_append[j])
            else:
                stack.append(c)
        return ''.join(stack)
