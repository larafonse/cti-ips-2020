def count_words(text):
  text = text.replace(',','').replace(',','').replace('.','').replace('!','').replace('?','').lower().split()
  wordCount ={}
  
  i= 0
  temp =''
  for word in text:
    if word in wordCount:
      wordCount[word]+=1
    else:
      wordCount.update({word:1})
    
  finalString=""
  for x,y in wordCount.items():
    finalString = finalString + x+ " "+str(y)+"\n"

  return(finalString)
count_words("I do not like green eggs and ham, I do not like them, Sam-I-Am")