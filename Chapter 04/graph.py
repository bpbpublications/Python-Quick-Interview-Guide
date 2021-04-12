from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)#Create empty dictionary

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)#Add v2  to list of v1
        self.graph[v2].append(v1)#Add v1  to list of v2

    def printGraph(self):
        for node in self.graph:
            print(node,':',end=' ')#print vertex-id:
            for v in self.graph[node]:#print every vertex in the list
                print(v,end=' ')
            print('\n')#print new line at end of the list

#Driver code
g = Graph()

g.insertEdge('a', 'b')
g.insertEdge('b', 'c')
g.insertEdge('b', 'd')
g.insertEdge('d', 'e')

g.printGraph()