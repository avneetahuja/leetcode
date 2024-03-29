class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        for i in range(len(arr2)):
            map[arr2[i]] = i
        li = [[]for i in range(len(map)+1)]
        for a in arr1:
            if a in map:
                li[map[a]].append(a)
            else:
                li[-1].append(a)
        li[-1].sort()
        res = []
        for i in range(len(li)):
            for j in range(len(li[i])):
                res.append(li[i][j])
        return res

        
