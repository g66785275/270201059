def binary(a,lis):
  lis.sort()
  index1 = -1
  half1 = lis[:int(len(lis)/2)]
  half2 = lis[int(len(lis)/2):]
  for index in range(len(half1)):
    if a> half2[index]:
      binary(a,half2)
    elif a<half2[index]:
      binary(a,half1)
    else:
      index1 = index
  if index1 == -1:
    return False
  else:
    return True


print(binary(5,[5,7,8,9]))