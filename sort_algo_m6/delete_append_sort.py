# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
def da_sort(nums):
  temp_ar = sorted(nums)
  i, j = 0,0
  count = 0
  while i < len(nums):
    if nums[i] != temp_ar[j]:
      count+=1
      i+=1
    else:
      i+=1
      j+=1
      
  return count
  

da_sort([1, 5, 6, 2, 4, 3])