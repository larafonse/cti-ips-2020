### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  def insert(self, data, index):
    
    temp = LinkedList()
    curr = self.head
    last_index = True
    i = 0
    while curr!= None:
      if i == index:
        last_index =False
        print(data)
        temp.append(data)
      else:
        print(curr.data)
        temp.append(curr.data)
        curr = curr.next
      i+=1
      
    if last_index:
      temp.append(data)
      
    self.head = temp.head
    
    
    
    

    
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])
ll.insert(100,6)
print(ll.get(6))