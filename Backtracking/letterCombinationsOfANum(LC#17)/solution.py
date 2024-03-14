class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        n = len(digits)
        def f(i,li):
            if i==n:
                res.append(li)
                return
            string = keyboard[digits[i]]
            for c in string:
                f(i+1,li+c)
        f(0,"")
        return res
