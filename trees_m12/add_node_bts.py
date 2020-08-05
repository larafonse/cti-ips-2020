class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None

  def print_bfs(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      print(current_node.data)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

  def in_order_traversal(self):
    nodes = []
    def dfs(node):
      if node:
        
        dfs(node.left)
        nodes.append(node.data)
        dfs(node.right)

        
    dfs(self.root)
    return nodes
    
  def add(self,node):
    if not self.root:
      self.root = node
      return
    
    
    queue = [self.root]
    
    while len(queue)>0:
      current_node = queue.pop(0)
      if current_node.data > node.data and not current_node.left:
        current_node.left = node
        return  
      if current_node.data < node.data and not current_node.right:
        current_node.right = node
        return
      
      if current_node.data > node.data and current_node.left:
        queue.append(current_node.left)
      if current_node.data < node.data and current_node.right:
        queue.append(current_node.right)
      
      
      
    
  
tree = Tree()


tree.add(Node(8))
tree.add(Node(9))
tree.add(Node(7))

tree.add(Node(6))

tree.add(Node(3))
tree.add(Node(4))
print(tree.in_order_traversal())