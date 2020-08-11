## Given this recursive solution to the longestPalindrome problem,
## Start by writing out the recursive tree of function calls to understand the problem
## then, think about how you might turn this into an iterative solution.
def longestPalindrome(s):
  n = len(s)
  
  table = [[0 for x in range(n)] for y in range(n)]
  
  i = 0 
  maxLength = 1
  while i < n:
    table[i][i] = True
    i+=1
  
  
  start = 0
  i = 0 
  
  while i < n - 1:
    if (s[i] == s[i + 1]):
      table[i][i + 1] = True
      start = i
      maxLength = 2
    i = i + 1
    
  k = 3
  
  while k <= n:
    i = 0
    
    while i < (n - k + 1): 
      
      j = i + k -1
      
      if(table[i+1][j-1]) and (s[i] == s[j]):
        table[i][j] = True
        
        if k > maxLength : 
          start = i
          maxLength = k
      
      i +=1
    k +=1
    
  
  
  
  return s[start:start + maxLength+1] if s[start:start + maxLength+1][-1] !='x'else s[start:start + maxLength]

print(longestPalindrome("abbababootttoo"))## Given this recursive solution to the longestPalindrome problem,
## Start by writing out the recursive tree of function calls to understand the problem
## then, think about how you might turn this into an iterative solution.
def longestPalindrome(s):
  n = len(s)
  
  table = [[0 for x in range(n)] for y in range(n)]
  
  i = 0 
  maxLength = 1
  while i < n:
    table[i][i] = True
    i+=1
  
  
  start = 0
  i = 0 
  
  while i < n - 1:
    if (s[i] == s[i + 1]):
      table[i][i + 1] = True
      start = i
      maxLength = 2
    i = i + 1
    
  k = 3
  
  while k <= n:
    i = 0
    
    while i < (n - k + 1): 
      
      j = i + k -1
      
      if(table[i+1][j-1]) and (s[i] == s[j]):
        table[i][j] = True
        
        if k > maxLength : 
          start = i
          maxLength = k
      
      i +=1
    k +=1
    
  
  
  
  return s[start:start + maxLength+1] if s[start:start + maxLength+1][-1] !='x'else s[start:start + maxLength]

print(longestPalindrome("abbababootttoo"))