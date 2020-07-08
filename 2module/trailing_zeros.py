def fast_trailing_zero_factorial(n):
  i = 5
  count = 0
  while(n/i >= 1):
    count+=(n//i)
    i*=5
  return count

if __name__ == "__main__":
  
  print(fast_trailing_zero_factorial(int(input())))