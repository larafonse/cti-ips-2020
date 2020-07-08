def minAddToMakeValid(S):
  if S == '': return 0
  start = S[0]
  count = 1
  for i  in range(1,len(S)):
    if start == '(' and S[i]==')':
      count-=1
      start = S[i]
    else:
      start = S[i]
      count+=1
      
  return(count)
	
sampleInput = '()))(('
print(minAddToMakeValid(sampleInput))