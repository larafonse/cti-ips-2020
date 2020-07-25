def bigram_frequency_analyzer(text):
  frequency = {}
  text = text.split()


  for i in range(0,len(text)-2,1):
    if text[i]+" " +text[i+1] not in frequency:
      frequency.update({text[i]+" " +text[i+1]:{text[i+2]:1}})
    else:
      if text[i+2] in frequency[text[i]+" " +text[i+1]]:
        frequency[text[i]+" " +text[i+1]][text[i+2]]+=1
      else:
        frequency[text[i]+" " +text[i+1]].update({text[i+2]:1})
    
    
  bigram = ""
  for x,y in frequency.items():
    final = ""
    for z,w in y.items():
      final=final+" "+z +" ("+str(w)+")"
      
    bigram = bigram + x+" :"+final +" \n"
  
  return(bigram)
  
test ="I do not like green eggs and ham, I do not like them, Sam-I-Am! I do not like them with a fox, I do not like them in a box. I do not like them here or there, I do not like them anywhere! I do not like them, Sam-I-Am, I do not like green eggs and ham!"
  
print(bigram_frequency_analyzer(test))