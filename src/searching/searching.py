# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    if target == arr[i]:
      return i
  return -1 # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1
    
  low = 0
  high = len(arr) - 1
  mid = (low+high) // 2

  found = False
  while low <= high:
    if arr[mid] > target:
      high = mid-1
    elif arr[mid] < target:
      low = mid+1
    else:
      found = True
      break
    mid = (low+high) // 2

  if found:
    return mid
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high) // 2

  if len(arr) == 0:
    return -1
  # TO-DO: add missing if/else statements, recursive calls
