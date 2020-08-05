def k_backspace(inputString):
  i = 0
  temp = ''
  while i < len(inputString):
    if inputString[i] == '<':
      temp = temp[:-1]
    else:
      temp +=inputString[i]
    i+=1
  
  return temp
	

# don't forget to actually call your answer's function!
testInput = 'a<bc<'
actualOutput = k_backspace(testInput)
print(actualOutput)