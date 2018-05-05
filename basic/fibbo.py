import time
def fib(n):
  fibtable={}
  fibtable[0]=0
  fibtable[1]=1
  for i in range(2,n+1):
    fibtable[i]=fibtable[i-1]+fibtable[i-2]
  #print(fibtable)
  return fibtable
a = time.time()
ans=fib(100000)
#for i in ans.values():
#  print(i)
print(time.time()-a)