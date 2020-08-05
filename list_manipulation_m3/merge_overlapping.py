def merge_overlapping_intervals(intervals):
  if 0<=len(intervals)<=1:
    return intervals
    
  lis= []
  index= []
  c1, c2= intervals[0][0],intervals[0][1]
  for i in range(len(intervals)-1):
    if c2 >= intervals[i+1][0]:
      c2= intervals[i+1][1]
    else:
      lis.append([c1,c2])
      c1,c2 = intervals[i+1][0],intervals[i+1][1]
  
  lis.append([c1,c2])
  return(lis)
    
    
  return intervals

print(merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]]))  
    
    
  