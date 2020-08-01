def sentiment_scores(sentiments, texts):
  sentiment_list =[]
  
  for text in texts:
    feeling = 0
    text_list = text.replace("!","").replace(".","").replace(",","").split()

    for word in text_list:

      if word in sentiments:

        feeling +=sentiments[word]
      
    sentiment_list.append(feeling)
  
  return(sentiment_list)


sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}

texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]


sentiment_scores(sentiments,texts)