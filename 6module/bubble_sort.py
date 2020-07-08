def bubble_sort_swaps(nums):
  swapped = True
  count=0
  
  while swapped:
    swapped=False
    for i in range(len(nums)-1):
      if nums[i]>nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        swapped=True
        count+=1
    
  return count
    

print(bubble_sort_swaps([6,2,4,3]))