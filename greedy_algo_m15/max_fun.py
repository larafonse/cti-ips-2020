def maximize_fun(activities, start, end):
  selected_activities = [activities[0]]
  k = 0 
  
  for i in range(1,len(activities)):
    if end[k]<=start[i]:
      selected_activities.append(activities[i])
      k = i
  
  
  return(selected_activities)
  
  
  
activities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
start = [0,1,5,6,8,10,11]
end =   [2,4,6,8,11,12,20]

maximize_fun(activities, start, end)