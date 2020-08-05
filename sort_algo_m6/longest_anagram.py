def longest_anagram(string,dictionary):
  count = [0 for x in range(len(dictionary))]
  for i in range(len(dictionary)):
    temp = [letter for letter in string]
    word = [letter for letter in dictionary[i]]
    print(temp,word)
    for letter in word:
      if letter in temp:
        count[i]+=1
        temp.remove(letter)
      else:
        count[i] = 0
        break
      
  return dictionary[count.index(max(count))]

print(longest_anagram('batman',['bat','aman','antman']))