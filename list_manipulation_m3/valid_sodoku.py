
def validate_sudoku_board(board):
  for row in board:
    for i in range(9):
      if row[i]=='.':
        continue
      if not inRow(row,row[i]):
        return False
      if not inColumn(board, i,row[i]):
        return False
  return True

def inRow(arr, n):
  print(n)
  count=0
  for i in arr:
    if i ==n:
      count+=1
  return True if count <2 else False
  
def inColumn(board, index, n):
  count = 0
  for row in board:
    if row[index] == n:
      count+=1
  return True if count <2 else False
      

print(validate_sudoku_board([[5,3,".",'.','.',7,'.','.','.'],[5,'.',".",1,9,5,'.','.','.'],['.',9,8,'.','.','.','.',6,'.'],[8,'.',".",'.',6,'.','.','.',3],[4,'.',".",8,'.',3,'.','.',1],[7,'.',".",'.',2,'.','.','.',6],['.',6,".",'.','.','.',2,8,'.'],['.','.',".",4,1,9,'.','.',5],['.','.',".",'.',8,'.','.',7,9]]))
      
