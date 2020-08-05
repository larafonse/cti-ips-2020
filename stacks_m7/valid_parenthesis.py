def valid(parentheses):
  vals = [x for x in parentheses]
  dic = {
    '{':'}',
    '[':']',
    '(':')'
  }
  ends = ['}',']',')']
  
  current = vals[0]
  i = 1 
  
  while i < len(vals):
    if current in ends:
      current = vals[i]
    elif vals[i] == dic[current]:
      i+=1
      if i > len(vals)-1:
        break
      current = vals[i]
    elif vals[i] not in ends:
      current = vals[i]
    elif vals[i] in ends and vals[i]!=dic[current]:
      return False
    i+=1
    
  return True
  
  
print(valid('()[]{}'))