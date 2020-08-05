def rotate_matrix(matrix):
  x = 0
  y = 0
  z = len(matrix)-1
  l = z
  while x < len(matrix)//2:
    corners(matrix,x,y,z)
    x+=1
    y=x
    z-=1

  x = 0
  z = l
  w = 1
  
  while w<z:
    for u in range(w,z):
      rot(matrix,x,u,l)
    print('sss')
    x+=1
    w+=1
    z-=1
def corners(matrix, x,y, g):
  matrix[x][g], temp = matrix[x][y], matrix[x][g]
  matrix[g][g],temp = temp, matrix[g][g]
  matrix[g][y], matrix[x][y]= temp, matrix[g][y]
  return matrix

def rot(matrix,x,y,z):
  

  matrix[y][z-x], temp = matrix[x][y],matrix[y][z-x]
  matrix[z-x][z-y], temp = temp, matrix[z-x][z-y]
  
  matrix[z-y][x], matrix[x][y]= temp, matrix[z-y][x]
  return matrix




x = 1
y =4
arr =[]
for _ in range(3):
  arr.append([x for x in range(x,y)])
  x+=2
  y+=2