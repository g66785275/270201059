one = input("Enter a number:")
two = input("Enter a number:")
index1 = 0
length = min(len(one),len(two))
for _ in range(length) :
  if one[_] == two[_]:
    index1 += 1
print(index1)