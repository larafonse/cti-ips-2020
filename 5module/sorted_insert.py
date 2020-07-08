def find_index(sorted_list, target):
  
  low, high = 0, len(sorted_list)-1
  n =len(sorted_list)-1
  while low <=high:
    if sorted_list[low] >= target:
      return low
    if sorted_list[high] == target or (high-low == 1):
      return high
    if sorted_list[high]<target:
      return high+1
    
    mid = (low+high)//2
  
    
    if sorted_list[mid] == target:
      
      return mid
      
    if sorted_list[mid]>target:
      high = mid
    else:
      low = mid
      
  return mid
  
  
print(find_index([1,3,5,9],7))