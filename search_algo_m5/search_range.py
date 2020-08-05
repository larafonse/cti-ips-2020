def search_for_range(array, target):
  f_arr = [-1,-1]
  low, high = 0, len(array)-1
  while low <=high:
    if array[low] == target and f_arr[0] ==-1:
      f_arr[0]=low
    elif f_arr[0]==-1:
      low +=1
    if array[high]== target and f_arr[1] ==-1:
      f_arr[1]=high
    elif f_arr[1]==-1:
      high -=1
      
    if f_arr[0]!=-1 and f_arr[1]!=-1:
      return f_arr
    
  return f_arr
      
print(search_for_range([5,6,6,7,8], 6))