class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def f(li, i, s):
            if s == 0:
                res.append(li)
                return
            if s <= 0:
                return

            prev = -1
            for ind in range(i, len(candidates)):
                if candidates[ind] == prev:
                    continue
                f(li + [candidates[ind]], ind + 1, s - candidates[ind])
                prev = candidates[ind]

        f([], 0, target)
        return res
