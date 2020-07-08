def last_factorial_digit(n):
  x = 1
  for i in range(n,0,-1):
    x*=i
  return(x%10)
  
if __name__ == "__main__":
  print(last_factorial_digit(int(input())))