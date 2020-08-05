class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  def subgraph(self, root):
    to_visit = [root]

    visited = set()

    while len(to_visit) > 0:
      node = to_visit.pop(0)
      if node not in visited:
        
        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited
    
  def suggest_friends(self, me):
    
    
    my_friends = set(self.members[me])
    
    pontentials = {}
    
    for friend in my_friends:
      for their_friend in self.members[friend]:
        if their_friend not in my_friends and their_friend is not me:
          
          
          friendship_score = len(set(self.members[their_friend]).intersection(my_friends))
          
          if pontentials.get(friendship_score):
            pontentials[friendship_score].add(their_friend)
            
          else:
            pontentials[friendship_score] = {their_friend}
            
    
    
    scores = list(pontentials.keys())
    
    scores.append(0)
    
    best_score = max(scores)
    
    
    return(pontentials.get(best_score,set()))
          