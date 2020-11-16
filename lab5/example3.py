one = input("Enter a number:")
two = input("Enter a number:")
index1 = 0
length = min(len(one),len(two))
for i in range(length) :
  if one[i] == two[i]:
    index1 += 1
print(index1)