def generate_parentheses(n):
  
  parens = ['()']
  
  if n == 1:
    return(parens)
    
  
  last_set = set(parens)
  i=1
  
  while i<n:
    curr_set = set()
    
    for permutation in last_set:
      
      for p in range(len(permutation)):
        print(permutation,permutation[:p]+'()'+permutation[p:])
        curr_set.add(permutation[:p]+'()'+permutation[p:])
    
    last_set = curr_set
    i+=1
  
  
  return(sorted(last_set))
  
  

print(generate_parentheses(3))