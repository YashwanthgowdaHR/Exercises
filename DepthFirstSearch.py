from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        print("v: ", v, "visited: ", visited)
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            print("visited[",i,"]: ",visited[i])
            if visited[i] == False:
                self.DFSUtil(i, visited)

    #dfs for graph having cycle or loop
    """
    def DFS(self, v):
        visited = [False]*(len(self.graph))
        self.DFSUtil(v, visited)
    """
    
    def DFS(self):
        V = len(self.graph)
        visited = [False]*(V)
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
    

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is DFS from (starting from vertex 0)")
print(g.graph)
g.DFS()