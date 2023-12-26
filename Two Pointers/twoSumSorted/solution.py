class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1=0
        p2=len(numbers)-1
        while p1<p2:
            s = numbers[p1] + numbers[p2]

            if s == target:
                return [p1+1,p2+1]
            if s < target:
                p1+=1
            else:
                p2-=1
        return -1
