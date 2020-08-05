### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
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
  
  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
  def to_array(self):
    array = []
    curr = self.head
    while curr != None:
      array.append(curr.data)
      curr = curr.next
    return array
  
  # implement this method
  def reverse(self):
    prev_node = None
    
    curr = self.head  
    curr_next = curr.next
    
    while curr_next != None:
      
      curr.next = prev_node
      prev_node = curr
      curr = curr_next
      curr_next = curr_next.next
      
    curr.next = prev_node
    self.head = curr
  
    
ll = LinkedList()

ll.extend([1,2,3,4,5])

ll.reverse()