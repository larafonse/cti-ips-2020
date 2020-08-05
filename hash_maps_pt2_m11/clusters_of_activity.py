def find_center(matrix):
  center_val = 0
  center = None
  for key, val in matrix.items():
    if val>center_val:
      center = key
      center_val=val
  
  return(center)



reported_outbreak = {
  "5,5": 10,
  "5,6": 8,
  "5,4": 8,
  "4,5": 8,
  "4,5": 8,
  "4,6": 8,
  "6,6": 7,
  "6,5": 8,
  "4,4": 8,
  "3,4": 4,
  "3,3": 2,
  "6,7": 2
}

print(find_center(reported_outbreak))