class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] + gain
        highest = 0
        for i in range(len(gain)):
            res[i+1] = res[i] + gain[i]
            highest = max(highest,res[i+1])
        return highest
