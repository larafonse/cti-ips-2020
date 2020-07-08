import math
def Log3(n):
  return (math.log10(n)/math.log10(3)) if n!=0 else False
  
def power_of_three(n):
  return(math.ceil(Log3(n)) == math.floor(Log3(n)))


if __name__ == "__main__":
  print(power_of_three(int(input())))