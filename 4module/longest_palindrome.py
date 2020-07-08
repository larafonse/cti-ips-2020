def longest_palindrome(input_string):
  input_string=input_string.replace(" ",'')
  lonPal = ''
  # iterate though each letter
  for i in range(len(input_string)-1):
    temp = input_string[i]
    for j in range(i+1,len(input_string)):
      temp += input_string[j]
      if temp == temp[len(temp)::-1] and len(temp)>len(lonPal):
        lonPal = temp
    
  # add the letter to string and check if pali
  return lonPal

print(longest_palindrome("i want to be a racecar driver"))