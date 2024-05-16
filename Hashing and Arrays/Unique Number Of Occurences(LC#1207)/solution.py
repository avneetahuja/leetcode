class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for n in arr:
            counts[n] = 1+ counts.get(n,0)
        values = {}
        for n in counts.values():
            if n in values:
                return False
            values[n] = n
        return True
