def binary(a,lis):
  lis.sort()
  index1 = -1
  half1 = lis[:int(len(lis)/2)]
  half2 = lis[int(len(lis)/2):]
  if a>half2[0]:
    return binary(a,half2)
  elif a<half2[0]:
    return binary(a,half1)
  else:
    return True
  return False


print(binary(3,[5,7,8,9]))