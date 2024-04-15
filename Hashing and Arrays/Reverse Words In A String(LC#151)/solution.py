class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        li.reverse()
        return " ".join(li)
