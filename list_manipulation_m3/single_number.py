from collections import Counter

def single_number(integers):
  # c = Counter(integers)
  # for i in c:
  #   if c[i]==1:
  #     return i
  a = 0
  for i in integers:
    a^=i
  return a
