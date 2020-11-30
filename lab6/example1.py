
a = input("E-mail:")
a = a.lower()
a.split("@")
one = a[0]
two = a[1]
one = one.replace(".","")
a = one + "@"+two
if a =="ceng113@example.com":
  print("Yes")
else:
  print("No")


