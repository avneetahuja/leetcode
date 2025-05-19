class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        # print(" ".join([])=="")
        def f(idx,temp):
            if idx == len(s):
                ans.append(" ".join(temp))
                return
            word = ""
            for i in range(idx,len(s)):
                word += s[i]
                if word in wordDict:
                    temp.append(word)
                    f(i+1,temp)
                    temp.pop()
        f(0,[])
        return ans
