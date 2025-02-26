class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        seen =defaultdict(int)
        s = 0
        max_outlier = float(-inf)
        for i,n in enumerate(nums):
            s+=n
            seen[n]+=1
        for i,n in enumerate(nums):
            curr_sum = s
            curr_sum-=n
            if curr_sum/2 in seen:
                if curr_sum/2==n and seen[n]<2:
                    continue
                max_outlier = max(max_outlier, n)
        return max_outlier

