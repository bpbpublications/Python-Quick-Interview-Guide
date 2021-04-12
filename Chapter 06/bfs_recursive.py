#BFS iterative approach
from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def setEdge(self, u, v):
        self.graph[u].append(v)
    def bfs(self,node):
        self.visited = set()
        self.q = deque()
        self.q.append(node)
        self.recursiveBFS()

    def recursiveBFS(self):
        if not self.q:
            return
        # pop front node from queue and print it
        v = self.q.popleft()
        print(v, end=' ')
        # do for every edge (v -> u)
        for u in self.graph[v]:
            if u not in self.visited:
                # mark it visited and push it into queue
                self.visited.add(u)
                self.q.append(u)
        self.recursiveBFS()


g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)