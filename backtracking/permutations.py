def get_permutations(input_list):
  
  output = []
  
  if len(input_list)== 0:
    return output
    
  if len(input_list)==1:
    return [input_list]
    
  
  for i in range(len(input_list)):
    element = input_list[i]
    rest_list = input_list[:i]+input_list[i+1:]
    
    for p in get_permutations(rest_list):
      output.append([element]+p)
  
  
  return(output)
  
    
print(get_permutations([1,2,3]))