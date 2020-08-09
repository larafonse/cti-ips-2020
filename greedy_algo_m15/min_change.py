den = [10000, 5000, 1000, 500, 100, 50, 25, 10, 5, 1]

def get_change(N):
  change = []
  for num in den:
    if num < N:
      amount = N//num
      N-=(num*amount)
      for _ in range(amount):
        change.append(num)
      
      
  return(change)
  
  
get_change(370)