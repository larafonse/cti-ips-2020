def hammingDistance(x, y):
  z = x ^ y
  setBits = 0
  
  while (z > 0) : 
      setBits += z & 1
      z >>= 1
      
  return setBits  

    
testX = 4
testY = 1
testResult = hammingDistance(testX, testY)
print(testResult)