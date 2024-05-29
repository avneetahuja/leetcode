class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i in range(len(equations)):
            adjList[equations[i][0]].append((equations[i][1], values[i]))
            adjList[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        def search(source, destination, running_product):
            if source not in adjList or destination not in adjList:
                return -1.0
            
            if source == destination:
                return 1.0
            
            visited = set()
            stack = [(source, 1.0)]
            
            while stack:
                current, current_product = stack.pop()
                if current == destination:
                    return current_product
                visited.add(current)
                
                for neighbor, weight in adjList[current]:
                    if neighbor not in visited:
                        stack.append((neighbor, current_product * weight))
            
            return -1.0
        
        answers = []
        for query in queries:
            result = search(query[0], query[1], 1)
            answers.append(result)
        
        return answers
