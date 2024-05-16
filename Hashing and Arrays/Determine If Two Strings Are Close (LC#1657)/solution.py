class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        if n!=m:
            return False
        counts1,counts2 = {},{}
        for c in word1:
            counts1[c] = 1 + counts1.get(c,0)
        for c in word2:
            counts2[c] = 1 + counts2.get(c,0)
        return sorted(counts1.values()) == sorted(counts2.values()) and sorted(counts1.keys()) == sorted(counts2.keys())
