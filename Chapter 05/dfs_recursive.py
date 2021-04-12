#DFS iterative approach
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
        
    def DFS(self,node):
        self.visited = set() # Set to keep track of visited nodes.
        self.dfs(node)
        
    def dfs(self,node):
        if node not in self.visited:
            print (node,end=" ")
            self.visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)
#Driver code
g = Graph()
'''
g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)
'''
g.insertEdge(0,1)
g.insertEdge(0,3)
g.insertEdge(1,2)
g.insertEdge(1,3)
g.insertEdge(1,5)
g.insertEdge(1,6)
g.insertEdge(2,3)
g.insertEdge(2,4)
g.insertEdge(2,5)
g.insertEdge(3,4)
g.insertEdge(4,6)
'''
g.insertEdge(0, 1) 
g.insertEdge(0, 2) 
g.insertEdge(1, 2) 
g.insertEdge(2, 0) 
g.insertEdge(2, 3) 
g.insertEdge(3, 3) 

g.insertEdge(1, 0);  
g.insertEdge(0, 2);  
g.insertEdge(2, 1);  
g.insertEdge(0, 3);  
g.insertEdge(1, 4); 
'''
g.DFS(0)