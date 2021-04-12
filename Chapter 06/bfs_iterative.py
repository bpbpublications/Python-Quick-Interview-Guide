#BFS iterative approach
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

g = Graph()
g.addedge(2, 1)
g.addedge(2, 5)
g.addedge(5, 6)
g.addedge(5, 8)
g.addedge(6, 9)

g.bfs(2)