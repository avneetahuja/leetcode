class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_sum = 0
        def findMaxDepth(el):
            max_depth = 1
            for element in el:
                if not element.isInteger() and len(element.getList())>0:
                    max_depth = max(max_depth,1+findMaxDepth(element.getList()))
            return max_depth
        def findWeightedSum(li,depth,max_D):
            nonlocal depth_sum
            for element in li:
                if element.isInteger():
                    print(element.getInteger(),depth)
                    depth_sum+=element.getInteger()*(max_D-depth+1)
                elif len(element.getList())>0:
                    findWeightedSum(element.getList(),depth+1,max_D)
            
        max_D = findMaxDepth(nestedList)
        findWeightedSum(nestedList,1,max_D)
        return depth_sum
