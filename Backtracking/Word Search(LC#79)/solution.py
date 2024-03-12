class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def search(i,j,ind):
            
            if (i,j) in visited:
                return False
            if ind==len(word):
                return True
            visited.add((i,j))
            l,r,u,d = False,False,False,False
            if i-1>=0 and board[i-1][j]==word[ind]:
                u=search(i-1,j,ind+1)
            if j-1>=0 and board[i][j-1]==word[ind]:
                l=search(i,j-1,ind+1)
            if i+1<len(board) and board[i+1][j]==word[ind]:
                d =search(i+1,j,ind+1)
            if j+1<len(board[0]) and board[i][j+1]==word[ind]:
                r=search(i,j+1,ind+1)
            visited.remove((i,j))
            return l or r or d or u
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if search(i,j,1):
                        return True
        return False
