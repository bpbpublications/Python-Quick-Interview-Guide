from typing import List
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [0]*N
        pathgraph = defaultdict(list)
        for node1,node2 in paths:
            pathgraph[node1].append(node2)
            pathgraph[node2].append(node1)
        for i in range(1, N+1):       
            types = set([1,2,3,4])
            for neighbor in pathgraph[i]:
                if flowers[neighbor -1] in types:
                    types.remove(flowers[neighbor-1])
            flowers[i-1] = types.pop()
        return flowers
#Driver code
sol=Solution()
print(sol.gardenNoAdj(4,[[1,2],[2,3],[3,4],[1,3]]))
print(sol.gardenNoAdj(3,[[1,2],[2,3],[3,1]]))
print(sol.gardenNoAdj(4,[[1,2],[3,4]]))
print(sol.gardenNoAdj(4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
