a = int(input("How many numbers?"))
index = 0
for _ in range(a):
  number = int(input("Enter number:"))
  if number % 2 == 0 :
    index += 1
print((index/a)*100 ,"%")
