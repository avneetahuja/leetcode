class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # visited = {}
        # def search(i,j):
        #     visited[(i,j)] = True
        #     ## change to x later, dont expand if its in visited
        #     if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
        #         return False
        #     board[i][j]="X"
        #     west = True if board[i][j-1]=="X" else search(i,j-1)
        #     east = True if board[i][j+1]=="X" else search(i,j+1)
        #     south = True if board[i+1][j]=="X" else search(i+1,j)
        #     north = True if board[i-1][j]=="X" else search(i-1,j)
        #     if not(west and east and south and north):
        #         board[i][j] = "O"
        #         return False
        #     return True
        # for i in range(1,len(board)-1):
        #     for j in range(1,len(board[0])-1):
        #         if board[i][j]=="O" and (i,j) not in visited:
        #             search(i,j)
        def search(i,j):
            board[i][j]="#"
            # if i<0 or i>len(board)-1 or j<0 or j>
            #Corner points
            if (i==0 or i==len(board)-1)and (j==0 or j==len(board[0])-1):
                return
            if i+1 < len(board) and board[i+1][j]=="O":
                board[i+1][j]="#"
                search(i+1,j)
            if i-1 >=0 and board[i-1][j]=="O":
                board[i-1][j]="#"
                search(i-1,j)
            if j+1 < len(board[0]) and board[i][j+1]=="O":
                board[i][j+1]="#"
                search(i,j+1)
            if j-1 >=0 and board[i][j-1]=="O":
                board[i][j-1]="#"
                search(i,j-1)

                

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=="O":
                    search(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="#":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
