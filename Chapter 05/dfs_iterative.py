#DFS iterative approach
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        visited = set()
        st = []
        st.append(startNode)

        while(len(st)):
            cur = st.pop()
            if(cur not in visited):
                print(cur, end=" ")
                visited.add(cur)

            for vertex in self.graph[cur]:
                if(vertex not in visited):
                    st.append(vertex)
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