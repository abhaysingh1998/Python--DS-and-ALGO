import time

#Iterative approach using tables
def fib_I(n):
  fibtable={}
  fibtable[0]=0
  fibtable[1]=1
  for i in range(2,n+1):
    fibtable[i]=fibtable[i-1]+fibtable[i-2]
  #print(fibtable)
  return fibtable

a = time.time()

ans=fib_I(100000)
print(ans[100000])

print("Time Taken: ",time.time()-a)