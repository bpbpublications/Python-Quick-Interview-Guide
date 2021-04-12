from typing import List  
class Solution:
    def solution(self, board, word, x, y, cur):
        if(x < 0 or x >= len(board) 
           or y < 0 
           or y >= len(board[x]) 
           or board[x][y] == ' '):
            return False
        cur += board[x][y]

        if(len(cur) > len(word)):
            return False
        if(board[x][y] != word[len(cur)-1]):
            return False
        if(cur == word): return True
        temp = board[x][y]
        board[x][y] = ' '

        if(self.solution(board, word, x, y+1, cur)): return True
        if(self.solution(board, word, x, y-1, cur)): return True
        if(self.solution(board, word, x+1, y, cur)): return True
        if(self.solution(board, word, x-1, y, cur)): return True
        
        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if(len(word) == 0):
            return True
        n = len(board)
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if(word[0] == board[i][j] 
                   and self.solution(board, word, i, j, "")):
                    return True
        return False
temp =\
[
  ['A','B','C','X'],
  ['S','Z','C','S'],
  ['P','D','E','E']
]
sol=Solution()
#board=temp.copy();print(sol.exist(board,"ASFD"))
board=temp[:];print(sol.exist(board,"ABCCED"))
