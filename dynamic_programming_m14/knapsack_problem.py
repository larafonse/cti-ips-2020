def knapSack(W , wt , val , n): 
  
  cache = [[0 for _ in range(W+1)] for _ in range(n+1)]
  
  for x in range(n+1):
    for y in range(W+1):
      if x == 0 or y == 0:
        cache[x][y] == 0 
      elif wt[x-1] <= y: 
        cache[x][y] = max(val[x-1] + cache[x-1][y-wt[x-1]],  cache[x-1][y])
      else: 
        cache[x][y] = cache[x-1][y] 
  
  return cache[n][W] 
  
                   
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W , wt , val , n))