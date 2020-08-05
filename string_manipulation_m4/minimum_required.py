def minimumCharacters(word):
  count=0
  # check if its already a palindrome
  if word == reversed(word):
    return count
  else:
    count+=1
  # iterate through 
  temp = word
  rev =''
  for i in range(-1, -1*len(word),-1):
    rev = rev + word[i]
    revword = rev+word
    print(rev)
    if revword == revword[len(revword)::-1]:
      return count
    else:
      count+=1
      

  
print(minimumCharacters("ABC"))