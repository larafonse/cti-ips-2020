def merge_sorted_list(nums1, nums2):
  # declare indexes
  index1, index2 = 0, 0
  
  # loop while index2 is less than length of array
  while index2 < len(nums2):
  # if index2 val is less than index1 val or index1 val equal 0
    if nums2[index2] <= nums1[index1] or nums1[index1] == 0:
      nums1.insert(index1, nums2[index2]) # insert val2 in array1 at index1
      nums1.pop()                         # remove 0 
      index2+=1                           # increment index2 

  # else increment index1
    else:
      index1+=1
  return nums1


