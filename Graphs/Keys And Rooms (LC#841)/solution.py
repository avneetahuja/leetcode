class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        to_visit =[]
        def visit(i):
            if visited[i]:
                return
            visited[i]=True
            for room in rooms[i]:
                if not visited[room]:
                    to_visit.append(room)
            while len(to_visit)>0:
                visit(to_visit.pop())
        visit(0)
        # print(visited)
        for room in visited:
            if not room:
                return False
        return True
