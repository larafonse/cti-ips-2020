def merge_sort(nums):
  if len(nums)>1:
    mid = len(nums)//2
    
    right = nums[0:mid]
    left = nums[mid:]
    
    right = merge_sort(right)
    left = merge_sort(left)
    
    sorted_list = []
    
    while len(right) > 0 and len(left)>0:
      if right[0]>left[0]:
        sorted_list.append(left.pop(0))
      else:
        sorted_list.append(right.pop(0))
    sorted_list.extend(right)
    sorted_list.extend(left)
  
  else:
    sorted_list=nums
  return sorted_list