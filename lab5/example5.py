a = int(input("How many fibonacci numbers?"))
first = 1
second = 1
third = 2
for q in range(a):
  if a == 1 or a == 2:
    third = 1
    break
  elif a ==3:
    pass
for _ in range(a-3):
  third1 = third
  third = third + second
  second = third1
print(third)

