a = int(input("How many fibonacci numbers?"))
first = 1
second = 1
third = 2
if a == 1 or a == 2:
  third = 1
for _ in range(a-3):
  third1 = third
  third = third + second
  second = third1
print(third)

