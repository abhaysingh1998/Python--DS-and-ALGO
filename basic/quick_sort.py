def quicksort(v):
  if len(v) <= 1:
    return v

  pivot = v[len(v)//2]
  equals = [x for x in v if x == pivot]
  smaller = [x for x in v if x < pivot]
  higher = [x for x in v if x > pivot]

  return quicksort(smaller) + equals + quicksort(higher)
print(quicksort([5,3,7,1,0,8,9,2,4,6]))
