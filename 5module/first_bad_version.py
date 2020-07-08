# Although you cannot see it, imagine there is a function called isBadVersion already defined.
# the automatic tests will account for it
# here is an example implementation, although the tests will have a different actual value
# the first bad version won't always be 7, but the other function will behave similarly

# def isBadVersion(version):
#   return version > 7
# when you run your tests, comment this function out.

def firstBadVersion(last_version, isBadVersion):
  low, high = 0, last_version
  while low<=high:
    
    if not isBadVersion(low) and isBadVersion(high) and (high-low==1):
      print('hello')
      return high
    
    mid = (low+high)//2
    next = mid+1
    prev = mid-1
    print(high,low,mid,next,prev)
    if not isBadVersion(mid) and isBadVersion(next):
      return next
    if not isBadVersion(prev) and isBadVersion(mid):
      return mid
    
    if not isBadVersion(mid) and not isBadVersion(next):
      low = next
    if isBadVersion(mid) and isBadVersion(prev):
      high = prev



def isBadVersion(x):
  array = [False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
  
  return array[x-1]

last = [False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
print(firstBadVersion(len(last), isBadVersion))
for i in range(len(last)):
  if last[i]:
    print(i+1)
    break