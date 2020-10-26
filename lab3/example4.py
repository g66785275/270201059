age = float(input("Age:"))
if age < 6 or age > 60 :
  print("Free!")
elif  6 <= age < 18:
  print("Price: 1.5 TL.")
else:
  print("Price: 3 TL.")