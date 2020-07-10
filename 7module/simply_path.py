def simplifyPath(path):
  
  x, i=0,1
  stack = path[x]
  temp = '/'
  while i < len(path):

    if path[i].isalpha():
      stack = stack +path[i]
      x+=1
    elif path[i] == '/' and stack[x]!='/':
      stack = stack +path[i]
      x+=1
    elif path[i] == '.' and path[i+1]=='.':
      count =0   

      for j in range(-1,-1*(len(stack)-2) , -1):
        print(j, len(stack))
        if stack[j]=='/' and count == 1:
            temp = stack[:j]
            print(j)
            count+=1
        elif stack[j]=='/' and count <1:
            count+=1
        elif stack[j]=='/' and count >1:
            count +=1

      i+=1
      if count ==1:
          stack ='/'
      else:
          stack=temp
      x=len(stack)-1
      
    i+=1
      
      
  return stack if stack[-1]!='/' or len(stack)==1 else stack[:-1]

testPath = "/../"
testResult = simplifyPath(testPath)
print(testResult)