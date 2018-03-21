class item:
    def __init__ (self, ID, value, weight):
        self.ID = ID
        self.value = value
        self.weight = weight
        self.valueWeightRatio = value / weight
        self.taken = 0.0
 
 
def fillUpKnapsack (A, W):
    for i in A:
        if i.weight <= W:
            i.taken = 1.0
            W -= i.weight
        else:
            i.taken = W / i.weight
            W = 0
 
def printKnapsack (A):
    cost = 0.0
    for i in A:
        if i.taken > 0.0:
           print("Item ", i.ID, ": Value ", i.taken * i.value, " Weight ", int(i.taken * i.weight), sep = "")
           cost += i.taken * i.value
    print("Maximum Value: %d" %cost)

N = int(input("Number of Items: "))
W = int(input("Knapsack Capacity: "))
A = []
print ("Value Weight of: ")
for i in range (N):
    print ("Item ", i + 1, ": ", sep = "", end = "")
    v, w = [int (x) for x in input().split()]
    A.append(item(i + 1, v, w))
sorted(A,key=lambda x: x.valueWeightRatio, reverse = True)
cost = fillUpKnapsack (A, W)
print ("\n\nKnapsack Properties: ")
printKnapsack (A)