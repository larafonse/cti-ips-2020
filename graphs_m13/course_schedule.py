from collections import defaultdict 

def can_finish(num_courses, prerequisites):
  
  class_schedule = defaultdict(list) 
  
  for course in prerequisites:
    class_schedule[course[0]].append(course[1])
  
  good =set()
  def get_valid(node,used):
    if node in good:

      return(True)
    if node in used:
      
      return(False)
    else:
      
      used.add(node)
      for edge in class_schedule[node]:
        if edge in class_schedule and not get_valid(edge,used):
          return False
      good.add(node)
      
      return True
  
  for course in class_schedule:
    if course in good:
      continue
    if not get_valid(course,set()):

      return(False)
    good.add(course)
    
  return(True)
  

  


print(can_finish(3,[[1,0],[2,1]]))
      