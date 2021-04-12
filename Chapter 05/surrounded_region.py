from typing import List
class Solution:
	def solve(self, board: List[List[str]]) -> None:
		if not board:return None
        #Base cases
		if len(board)==1 or len(board)==2\
            or len(board[0])==1 or len(board[0])==2:
			return None
        #Function Converts all neighbours of i,j from O to P
		def dfs(board,i,j):
			if i<0 or j<0 or i>len(board)-1\
                or j>len(board[0])-1 or board[i][j]=='X':
				return
			if board[i][j]=='O':
				board[i][j]='P'
				dfs(board,i+1,j)
				dfs(board,i-1,j)
				dfs(board,i,j+1)
				dfs(board,i,j-1)
        #Convert all O's connected to top and bottom row to P
		for i in range(len(board[0])):
			if board[0][i]=='O': dfs(board,0,i)
			if board[len(board)-1][i]=='O':dfs(board,len(board)-1,i)
        #Convert all O's connected to top and bottom col to P
		for j in range(len(board)):
			if board[j][0]=='O': dfs(board,j,0)
			if board[j][len(board[0])-1]=='O':
				dfs(board,j,len(board[0])-1)
        #Scan the whole matrix, convert P to O, O to X
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j]=='O': board[i][j]='X'
				if board[i][j]=='P': board[i][j]='O'
#Driver code
b = [['X','X','X','X'],
     ['X','O','O','X'],
     ['X','X','O','X'],
     ['X','O','X','X']]
sol=Solution()
sol.solve(b)
for i in range(len(b)): print(b[i])