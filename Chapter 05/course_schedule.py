from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in prerequisites:
            G[i].append(j)
        self.color = { u : "white" for u in range(numCourses)  } 
        self.found_cycle = False   # - found_cycle is initially false
        for u in range(numCourses):# - Visit all nodes.
            c=self.color #Added for debugging
            if self.color[u] == "white":
                self.dfs_visit(G, u)
            if self.found_cycle:
                break
        return not self.found_cycle 
    def dfs_visit(self,G, u):
        c=self.color  #Added for debugging
        if self.found_cycle:return #End of recursion
        self.color[u] = "gray"  # - Gray nodes are in the current path
        for v in G[u]: # - Check neighbors,in adjacency list 
            
            if self.color[v] == "gray": # If neighbor is gray, there is loop
                self.found_cycle = True       
                return
            if self.color[v] == "white": # If neighbor is unvisited, call dfs_visit recursively.   
                self.dfs_visit(G, v)
        #pass
        self.color[u] = "black" #All neighbors visited             
sol=Solution()
#pre = [[0,1],[1,2],[2,3],[3,1]] 
#print(sol.canFinish(4,pre))   
pre = [[0,1],[0,2],[1,2]] 
#pre=[[0,1],[1,3],[1,4],[1,5],[0,2],[2,6],[2,7],[7,0]]
#pre=[[0,1],[1,3],[1,4],[1,5],[2,6],[2,7]]
print(sol.canFinish(3,pre))          
