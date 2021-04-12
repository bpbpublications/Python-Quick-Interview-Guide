from typing import List  
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if (N == 1): return 1
            else: return -1
        in_degree = [0]*(N+1)
        out_degree = [0]*(N+1)
        for edge in trust:
            in_degree[edge[1]] += 1
            out_degree[edge[0]] += 1
        for i in range(len(in_degree)):
            if (in_degree[i] == N-1) and (out_degree[i] == 0):
                return i
        return -1
#Driver code
sol = Solution()
print("Judge is ",sol.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
print("Judge is ",sol.findJudge(2,[[1,2]])) 
print("Judge is ",sol.findJudge(3,[[1,3],[2,3],[3,1]]))
print("Judge is ",sol.findJudge(2,[]))        