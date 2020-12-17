def binary_to_decimal(a):
  a = a[::-1]
  b = 0
  for q in range(0,len(a)):
    if a[q] == "1":
      b += 2**int(q)
    else:
      pass
  return str(b)
    
    
def decimal_to_binary(a):
  if a == 1:
      print("1")
  w = ""
  
  while a > 0:
    if a%2 == 1:
      w+="1"
    else:
      w+="0"
    a = a//2
  
  return w[::-1]


print(decimal_to_binary(25))
print(binary_to_decimal("11001"))