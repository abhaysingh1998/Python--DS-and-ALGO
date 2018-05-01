class Tree():
  def __init__(self,initval=None):
    self.value=initval
    if self.value:
      self.left=Tree()
      self.right=Tree()
    else:
      self.left=None
      self.right=None
    return
  def isempty(self):
    return(self.value==None)
  def inorder(self):
    if self.isempty():
      return([])
    else:
      return(self.left.inorder()+[self.value]+self.right.inorder())
  def __str__(self):  #just displays the inorder traversal :)
    return(str(self.inorder()))
  def find(self,v):
    if self.isempty():
      return False
    if self.value==v:
      return True
    if v<self.value:
      return self.left.find(v)
    else:
      return self.right.find(v)
  def minval(self):
    if self.left==None:
      return self.value
    else:
      return self.left.minval()
  def maxval(self):
    if self.right==None:
      return self.value
    else:
      return self.right.maxval()
  def insert(self,v):
    if self.isempty():
      self.value=v
      self.left=Tree()
      self.right=Tree()
    if self.value==v:
      return
    if v<self.value:
      self.left.insert(v)
      return
    if v>self.value:
      self.right.insert(v)
      return
  def delete(self,v):
    if self.isempty():
      return
    if v<self.value:
      self.left.delete(v)
      return
    if v>self.value:
      self.right.delete(v)
      return
    if self.value==v:
      if self.isleaf():
        self.makeempty()
      elif self.left.isempty:
        self.copyright()
      else:
        self.value=self.left.maxval()
        self.left.delete(self.left.maxval())
      return
  def makeempty(self):
    self.value=None
    self.left=None
    self.right=None
    return
  def copyright(self):
    self.value=self.right.value
    self.left=self.right.left
    self.right=self.right.right
    return
  def isleaf(self):
    return(self.left.isempty() and self.right.isempty())


t= Tree()
for i in [1,3,2,18,7,5,4,22,14]:
  t.insert(i)
print(t)
print(t.inorder())
t.delete(14)            #deletes 14 from the tree
print(t.inorder())                
print(t.inorder())     #prints tree (inorder)
print(t.find(4))       #True
print(t.find(100))     #False
print(t.minval())
print(t.maxval())