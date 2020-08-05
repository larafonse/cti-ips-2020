def reverse_bits(num):
  result = 0
        
  for i in range(32):
    temp = 1 << i
    temp = temp & num
    temp = temp >> i
    temp = temp << (31 - i)
    result = result | temp
            
  return result