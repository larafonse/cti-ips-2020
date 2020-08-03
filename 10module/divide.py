def divide(dividend, divisor):
  count= 0
  negative =False
  
  if ((dividend<0) ^ (divisor<0)):
    negative= True
    
  dividend, divisor= abs(dividend), abs(divisor)
  
  while dividend >= divisor:
    count+=1
    dividend -=divisor
  
  return count if not negative else count*-1
 
  
    
testX = 7
testY = -3
testResult = divide(testX, testY)
print(testResult)