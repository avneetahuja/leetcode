class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        dp = {}
        def search(word):
            if word in dp:
                return dp[word]
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in words and suffix in words) or (prefix in words and search(suffix)):
                    dp[word]=True
                    return True
            dp[word] = False
            return False

        for word in words:
            if search(word):
                res.append(word)
        return res
