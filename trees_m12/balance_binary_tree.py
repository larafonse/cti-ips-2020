import math

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

    ## INSTEAD, non binary
    self.children = []

    self.parent = None

class Tree:
  def __init__(self):
    self.root = None

  def in_order_traversal(self):
    i_o_t_arr = []
    def dfs(node):
      if node:
        dfs(node.left)
        i_o_t_arr.append(node.data)
        dfs(node.right)

    dfs(self.root)
    
    return(i_o_t_arr)

  def level_order_traversal(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      if current_node.left:
        queue.append(current_node.left)
      print(current_node.data)
      if current_node.right:
        queue.append(current_node.right)

  def add(self,node):
    if not self.root:
      self.root = node
      return 

    def insert(root, node):

      if root.data > node.data:
        if root.left is None:
          root.left = node
        else:
          insert(root.left, node)
      else:

        if root.right is None:
          root.right = node
        else:
          insert(root.right, node)
    
    insert(self.root, node)

  def height(self):

    def get_height(node):

      if node is None:
        return 0
      else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if left_height > right_height:
          return left_height +1
        else:
          return right_height +1
    return get_height(self.root)

  def balance(self):
    # write a function to reduce the height of this tree as much as possible
    if not self.root:
      return
    
    sorted_tree = self.in_order_traversal()
    
    mid = math.ceil(len(sorted_tree)/2)-1
    
    left_arr, right_arr, self.root = sorted_tree[:mid],sorted_tree[mid+1:],Node(sorted_tree[mid])
    
    def bal(arr):
      if len(arr) <= 0:
        return
      if len(arr) == 3:
        self.add(Node(arr[1]))
        self.add(Node(arr[0]))
        self.add(Node(arr[2]))
      elif len(arr) == 2:
        self.add(Node(arr[1]))
        self.add(Node(arr[0]))
      elif len(arr) == 1:
        self.add(Node(arr[0]))
      else:
        
        mid = math.ceil(len(arr)/2)-1
        left_arr, right_arr, temp_node = arr[:mid],arr[mid+1:],Node(arr[mid])
        self.add(temp_node)
        bal(right_arr)
        bal(left_arr)
        
    
        
      return
    
    bal(right_arr)
    bal(left_arr)
    print(left_arr,right_arr,self.root)

tree = Tree()

tree.root = Node(6)

tree.root.right = Node(27)

tree.root.right.left = Node(15)

tree.root.right.left.left = Node(10)

tree.root.right.left.left.left = Node(8)
tree.root.right.left.left.right = Node(13)


tree.level_order_traversal()
tree.balance()
tree.level_order_traversal()
