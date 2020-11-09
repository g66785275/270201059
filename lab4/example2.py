year = int(input("Year:"))
index = 0
if year % 4 == 0 : 
  if year % 100 == 0 :
    if year % 400 != 0 :
      print(" Not a Leap year!")
  else:
    print("Leap")

else:
  print("Not leap")

if year % 4 =0 0 and (year % 100 != 0 or year % 400 ==0):
  print("Leap")
else:
  print("Not leap.")

