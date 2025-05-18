import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c:[] for c in range(numCourses)}
        for c,p in prerequisites:
            graph[c].append(p)
        res = []
        visited,cycle = set(),set()
        def dfs(c):
            
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
