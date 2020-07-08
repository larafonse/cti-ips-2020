def strStr(haystack, needle):

  return len(haystack.split(needle)[0]) if needle in haystack else -1
  

print(strStr("hello",'ll'))