def color_sort(nums):
  one_index = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      nums.insert(0,nums.pop(i))
      one_index +=1
    elif nums[i] == 1:
      nums.insert(one_index, nums.pop(i))
    else:
      nums.append(2)
      nums.pop(i)
      if nums[i] == 1:
        nums.insert(one_index, nums.pop(i))
      if nums[i] == 0:
        nums.insert(0,nums.pop(i))
        one_index +=1

  return(nums)

print(color_sort([0,1,0,1,2,1]))