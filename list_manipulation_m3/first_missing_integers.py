def first_missing_positive_integer(integers):
  if max(integers)<0:
        return 1
  int_set = set(x for x in range(1,max(integers)+2)) - set(integers)
  
  return min(int_set)
  
print(first_missing_positive_integer([3,4,-1,1]))