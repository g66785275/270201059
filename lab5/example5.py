a = int(input("How many fibonacci numbers?"))
first = 1
second = 1
third = 2
for q in range(a):
  if a == 1 or a == 2:
    print(1)
    break
  elif a ==3:
    print(2)
    break
  else:
    third1 = third
    third = third + second
    second = third1
print(third)

