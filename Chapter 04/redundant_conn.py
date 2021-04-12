from typing import List  
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Create a parent array. Initially each node is its own parent
        p = [x for x in range(len(edges)+2)]
        
        #Function to return parent of x
        #Recursively call itself till we find that parent of x is x itself
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        #If parents of x and y are different make y as parent of x
        #Returns true if parents are same
        def union(x, y):
            if find(x) == find(y): return True
            p[find(x)] = find(y)
        #For source destination pairs of edge 
        #if both have same parent return the pait x,y
        for x, y in edges:
            if union(x,y): return [x, y]
        
#Driver code
sol=Solution()
edges = [[1,2], [1,3], [2,3]]
print(sol.findRedundantConnection(edges))
edges = [[1,2], [1,3]]
print(sol.findRedundantConnection(edges))
edges =[[1,2], [2,3], [3,4], [1,4], [1,5]]
print(sol.findRedundantConnection(edges))