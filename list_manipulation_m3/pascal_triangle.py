def pascal_triangle(n):
  # Create an empty list
  l1=[]
  for line in range(1,n+1):
    
    C = 1
    l2=[]
    
    for i in range(1, line + 1): 
      l2.append(C) 
      C = int(C * (line - i) / i)  
    l1.append(l2)
  return(l1)

