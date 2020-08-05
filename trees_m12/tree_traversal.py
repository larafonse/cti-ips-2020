class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class Tree:
  def __init__(self):
    self.root = None
    
    
  def level_order_traversal(self):
    # return the tree as a list in a level-order sequence
    
    if not self.root:
      return
    
    queue = [self.root]
    lot_arr = []
    
    while len(queue)>0:
      curr_node = queue.pop(0)
      lot_arr.append(curr_node.data)
      
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
      
    
    return lot_arr
    
    
    
  def pre_order_traversal(self):
    # return the tree as a list in a pre-order sequence (dfs)
    
    def dfs(node):
      if node:
        pot_arr.append(node.data)
        dfs(node.left)
        dfs(node.right)
        
    pot_arr=[]
    dfs(self.root)
    
    return pot_arr
    
  def in_order_traversal(self):
    # return the tree as a list in-order (dfs)
    def dfs(node):
      if node:
        dfs(node.left)
        iot_arr.append(node.data)
        dfs(node.right)
    
    iot_arr=[]
    dfs(self.root)
    
    return iot_arr
    
  def post_order_traversal(self):
    # return the tree as a list in a post-order sequence (dfs)
    def dfs(node):
      if node:
        dfs(node.left)
        dfs(node.right)
        pot_arr.append(node.data)
    
    pot_arr = []
    
    dfs(self.root)
    return pot_arr

tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

print(tree.level_order_traversal())
print(tree.pre_order_traversal())
print(tree.in_order_traversal())
print(tree.post_order_traversal())