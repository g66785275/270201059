day = int(input("Day:"))
month = input("month:")

if month == "march":
  if day < 21:
    print("Winter")
  else:
    print("Spring")
elif month == "may" or month == "april":
  print("Spring")
elif month == "june":
  if day < 21:
    print("Spring")
  else:
    print("Summer")
elif month == "july" or month == "agust":
  print("Summer")
elif month == "september":
  if day < 21:
    print("Summer")
  else:
    print("Fall")
elif month == "october" or month == "november":
  print("Fall")
if month == "december":
  if day < 21:
    print("Fall")
  else:
    print("Winter")
elif month == "february" or month == "january":
  print("Winter")
