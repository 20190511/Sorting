def RadixSort(array):
  temp = [0]*(max(array)+1)
  for item in array:
    temp[item] += 1

  newList = []
  for i in range (len(temp)):
    for j in range (temp[i]):
      newList.append(i)
  return newList
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(RadixSort(array))

    