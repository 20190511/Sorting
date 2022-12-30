def quickSort (array, start, end):
  if start >= end:
    return
  pivot = start
  left = start+1
  right = end
  while left <= right:
    while (left<=end and array[left]<=array[pivot]):
      left += 1
    while (right>=start+1 and array[right]>=array[pivot]):
      right -= 1
    if left > right: 
      array[pivot],array[right] = array[right],array[pivot]
    else: #같아도 바꿔주기.
      array[right],array[left] = array[left], array[right]

  quickSort(array,start,right-1)
  quickSort(array,right+1,end)



a = [5,7,9,0,3,1,6,2,4,8]
quickSort(a,0,len(a)-1)
print(a)