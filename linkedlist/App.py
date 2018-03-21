from LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertEnd(3)
linkedList.insertStart(31)

linkedList.traverseList()
print("Size is: ",linkedList.counter)
print("=============")
linkedList.remove(12)

linkedList.traverseList()
print("Size is: ",linkedList.counter)