from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def size(self):
        return self.counter

    def insertEnd(self, data):
        if self.head is None:
            self.insertStart(data)
            return
        self.counter += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
    
    def remove(self, data):
        self.counter -= 1
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)
