def removeOuterParentheses(string):
  temp = ""
  val =0
  for x in string:
    if x == '(':
      val+=1
      if val !=1:
        temp = temp+x
    else:
      val-=1
      if val !=0:
        temp= temp+x
      
  return temp

sampleInput = "(()())(())(()(()))"
print(removeOuterParentheses(sampleInput))