# reverses the first k elements of an array
def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
  
def pancake_sort(nums):
  sorted_nums = sorted(nums)
  k_values = []
  k = -1
  while nums != sorted_nums and k>=(len(nums)*-1):
    max_val = sorted_nums[k]
    if max_val == nums[k]:
      k-=1
      continue
    elif max_val == nums[0]:
      m = len(nums)+k+1
      flip(nums,m)
      k_values.append(m)
      k-=1
    else:
      for i in range(1,len(nums)):
        if nums[i] == max_val:
          flip(nums,i+1)
          k_values.append(i+1)
          break
    
  return(k_values)


print(pancake_sort([5,2,3,4,1,6]))