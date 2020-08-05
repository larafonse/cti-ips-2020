def rotate_array(input_array, k):
  for _ in range(k):
    n= input_array.pop()
    input_array.insert(0,n)

  # input_array = input_array[(-1*k):]+ input_array[:(-1*k)]
 

