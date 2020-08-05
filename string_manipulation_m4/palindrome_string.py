import re
def isPalindrome(word):
  temp = re.sub("[^0-9a-zA-Z]+", "",word).lower()
  tempRev = temp[len(temp)::-1]
  return 1 if temp==tempRev else 0

print(isPalindrome('A man, a plan, a canal, Panama.'))