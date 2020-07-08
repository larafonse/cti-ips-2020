def find_pivot_index(input_list):
  # declare low and high
  low, mid, high, n = 0,0,len(input_list)-1, len(input_list)-1
  
  while low <= high:
  # if low and high are the sorted return low
    if input_list[low] <=input_list[high]:
      return low
  # find the mid point, next , prev
    mid = (low + high)//2
    next, prev = (mid+1)%n, (mid-1)%n
    # if mid point is the same or lower than prev and next return mid
    if input_list[mid] <= input_list[next] and input_list[mid] <= input_list[prev]:
      return mid
    # if low val is less than mid val set mid to next
    if input_list[low] <= input_list[mid]:
      low = next
    # else set high to prev
    else:
      high = prev
  return -1
      


print(find_pivot_index([1,2,3]))