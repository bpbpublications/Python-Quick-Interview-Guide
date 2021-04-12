from typing import List
from collections import  deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * N for _ in range(M)]
        hasfind = False
        que = deque()
        for i in range(M):
            if hasfind: break
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    hasfind = True
                    break
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        visited[x][y] = 1
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x, y))
                        else:
                            continue
            step += 1
        return -1

    def dfs(self, A, i, j, visited, que):
        if visited[i][j]: return
        visited[i][j] = 1
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if A[i][j] == 1:
            que.append((i, j))
            A[i][j] = 2
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < M and 0 <= y < N:
                    self.dfs(A, x, y, visited, que)
#Driver code
A=[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
sol=Solution()
print(sol.shortestBridge(A)) 
A = [[0,1,0],[0,0,0],[0,0,1]]   
print(sol.shortestBridge(A))                 