class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")]+=1
            map[tuple(count)].append(s) #using the unique count as the key in hashmap
        return map.values()
