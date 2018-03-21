from collections import deque

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.adjacencyList = []

def bfs(startnode):
    q = deque()
    q.append(startnode)
    startnode.visited = True

    while q:
        actualnode = q.popleft()
        print(actualnode.name)
        for neighbour in actualnode.adjacencyList:
            if not neighbour.visited:
                neighbour.visited = True
                q.append(neighbour)

names = ['A','B','C','D','E','F']
nodes = []

for name in names:
    nodes.append(Node(name))

nodes[0].adjacencyList.append(nodes[1])
nodes[0].adjacencyList.append(nodes[2])
nodes[2].adjacencyList.append(nodes[3])
nodes[1].adjacencyList.append(nodes[4])
nodes[1].adjacencyList.append(nodes[5])

bfs(nodes[0])