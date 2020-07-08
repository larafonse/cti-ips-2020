def atoi(a):
  a = a.replace(" ", '')
  temp = ''
  for i in a:
    if i.isdigit() or i =='-':
      temp= temp + i 
    else:
      break
  if temp == '':
    return 0
  elif int(temp) < -231:
    return -2147483648
  else:
    return int(temp)

print(atoi("a-12ac2e12"))