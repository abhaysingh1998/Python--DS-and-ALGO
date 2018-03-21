import sys
import heapq

class Node:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacenciesList = []
        self.predecessor = None
        self.mindistance = sys.maxsize

    def __cmp__(self,othervertex):
        return self.__cmp__(self.mindistance,othervertex.mindistance)

    def __lt__(self, other):
        return self.mindistance < other.mindistance

class Edge:

    def __init__(self, weight, startvertex, endvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.endvertex = endvertex

def calculateshortespath(vertexlist, startvertex):
    q = []
    startvertex.mindistance = 0;
    heapq.heappush(q, startvertex)

    while q:
        actualnode = heapq.heappop(q)
        for edge in actualnode.adjacenciesList:
            tempdist = edge.startvertex.mindistance + edge.weight
            if tempdist < edge.endvertex.mindistance:
                edge.endvertex.mindistance = tempdist
                edge.endvertex.predecessor = edge.startvertex
                heapq.heappush(q,edge.endvertex)
def getshortestpath(targetvertex):
    print("The value of it's minimum distance is: ",targetvertex.mindistance)
    node = targetvertex
    while node:
        print(node.name)
        node = node.predecessor

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");
node7 = Node("G");
node8 = Node("H");

edge1 = Edge(5,node1,node2);
edge2 = Edge(8,node1,node8);
edge3 = Edge(9,node1,node5);
edge4 = Edge(15,node2,node4);
edge5 = Edge(12,node2,node3);
edge6 = Edge(4,node2,node8);
edge7 = Edge(7,node8,node3);
edge8 = Edge(6,node8,node6);
edge9 = Edge(5,node5,node8);
edge10 = Edge(4,node5,node6);
edge11 = Edge(20,node5,node7);
edge12 = Edge(1,node6,node3);
edge13 = Edge(13,node6,node7);
edge14 = Edge(3,node3,node4);
edge15 = Edge(11,node3,node7);
edge16 = Edge(9,node4,node7);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node1.adjacenciesList.append(edge3);
node2.adjacenciesList.append(edge4);
node2.adjacenciesList.append(edge5);
node2.adjacenciesList.append(edge6);
node8.adjacenciesList.append(edge7);
node8.adjacenciesList.append(edge8);
node5.adjacenciesList.append(edge9);
node5.adjacenciesList.append(edge10);
node5.adjacenciesList.append(edge11);
node6.adjacenciesList.append(edge12);
node6.adjacenciesList.append(edge13);
node3.adjacenciesList.append(edge14);
node3.adjacenciesList.append(edge15);
node4.adjacenciesList.append(edge16);

vertexlist = (node1,node2,node3,node4,node5,node6,node7,node8)

calculateshortespath(vertexlist,node1)
getshortestpath(node7)
