n = int(input())
index = 0
for a in range(n):
  for i in range(n):

    if i == index:
      print(1,end="")
    else:
      print(0,end="")
  index += 1  
  print("\n")
    
    
  
