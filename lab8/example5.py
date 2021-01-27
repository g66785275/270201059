def check(password):
  level = 0
  for a in password:
    if " " in password or len(password) < 8:
      print("Level",level)
  
  for a in password:
    if a.isnumeric():
      level+=1
      break
  

  for a in password:
    if a.isalpha():
      level+=1
      break
  for a in password:
    if a.isnumeric() or a.isalpha():
      pass
    else:
      level+=1
      break

  print("Level",level)