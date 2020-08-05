class Graph:
  def __init__(self):
    self.verticies = {}


  def add_node(self,node):
    self.verticies[node] = []


  def add_edge(self,node_a,node_b):
    self.verticies[node_a].append(node_b)
    self.verticies[node_b].append(node_a)
    
  def subgraph(self, start):
    # Implement the subgraph traversal
    queque = [start]
    
    visited = set()
    
    while len(queque)>0:
      curr_node = queque.pop(0)
      
      if curr_node not in visited:
        visited.add(curr_node)
        
        if curr_node in self.verticies:
          for neighbor in self.verticies[curr_node]:
            if neighbor not in visited:
              queque.append(neighbor)
              
    return(visited)
    
  
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')