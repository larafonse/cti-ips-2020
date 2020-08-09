def single_number(nums):
  ones = 0
  twos = 0
  n = len(nums)
  arr = nums
  for i in range(n): 
    twos = twos | (ones & arr[i]) 

    ones = ones ^ arr[i] 

    common_bit_mask = ~(ones & twos) 

    ones &= common_bit_mask 

    twos &= common_bit_mask 
    
  return ones
  



single_number([1, 2, 3, 1, 2, 3, 1, 2, 3, 4])