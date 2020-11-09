#import math
#a = int(input("A:"))
#b = int(input("B:"))
#print(math.pow(a,b))

a=int(input())
b=int(input())
total=a
for i in range(0,b-1):
  total*=a
print(total)