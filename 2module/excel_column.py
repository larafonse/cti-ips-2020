def excel_column_to_number(column):
  sum, count = 0,0
  
  for i in range(len(column)-1,-1,-1):
    sum += (26**count) * (ord(column[i]) - 64)
    count+=1
  return sum


if __name__ == "__main__":
  print(excel_column_to_number(input()))