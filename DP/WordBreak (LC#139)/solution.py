class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def f(idx):
            if idx == len(s):
                return True
            if idx in memo:           
                return memo[idx]

            word = ""
            for i in range(idx, len(s)):
                word += s[i]
                if word in wordDict and f(i+1):
                    memo[idx] = True  
                    return True

            memo[idx] = False        
            return False

        return f(0)
