def dailyTemperatures(dailyTemps):
	for x in range(len(dailyTemps)):
	  dailyTemps[x] = nextHottest(dailyTemps,x)
	return dailyTemps
	
def nextHottest(arr, n):
  hot = 0
  current = arr[n]
  for i in range(n+1, len(arr)):
    if current < arr[i]:
      hot+=1
      return hot
    else:
      hot+=1
      
  return 0
    
sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))