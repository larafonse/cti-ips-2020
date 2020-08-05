def matrix_search(matrix, target):
  if target > matrix[len(matrix)-1][len(matrix[0])-1]:
    return 0
  low, high= 0, len(matrix[0])-1, 
  i,n = 0,high
  while target>matrix[i][high]:
    i+=1
    
  while low <= high:
    if matrix[i][low]>target or matrix[i][high]<target:
      return 0
    if matrix[i][low] == target:
      return 1
    if matrix[i][high] == target:
      return 1
    if high-low == 1:
      return 0
    
    mid = (low+high)//2
    if matrix[i][mid] == target:
      return 1
    next = (mid+1)%n
    prev = (mid-1)%n
    
    if matrix[i][mid] <= target:
      low = next
    else:
      high = prev
    
print(matrix_search([[1,3,5,7],[10,11,16,20],[23,30,34,50]],2))