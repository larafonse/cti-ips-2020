def evaluate_expression(expression):
  stack = []
  
  for val in expression:
    if val.isdigit():
      stack.append(val)
    else:
      
      if val == '/':
        val ='//'
      val1 = stack.pop()
      val2 = stack.pop()
      
      result = str(eval(val2 +' '+ val+' '+val1))
      
      stack.append(result)
      
  return int(stack[0])

expression = ["3", "4", "/", "5", "*"]

print(evaluate_expression(expression))
print('*******************')
