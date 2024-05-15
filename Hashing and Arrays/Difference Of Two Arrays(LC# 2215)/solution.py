class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        values_1,values_2 = {},{}
        set1 = set()
        set2 = set()
        for n in nums1:
            values_1[n] = n
        for n in nums2:
            values_2[n] = n
        for n in nums1:
            if not n in values_2:
                set1.add(n)
        for n in nums2:
            if not n in values_1:
                set2.add(n)
        return [list(set1),list(set2)]
