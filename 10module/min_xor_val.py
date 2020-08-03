def min_xor_value(num):
  low = num[0]^num[1]
  
  for i in range(len(num)-1):
    if low > num[i]^num[i+1]:
      low = num[i]^num[i+1]
  
  return(low)
  
min_xor_value([1,2,3,4,5])