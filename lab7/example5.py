
while True:
  keyp=input(False)
  if len(keyp) < 8:
    print(False)
  else:
    if keyp.lower() == keyp:
      print(False)
    else:
      if keyp.upper() == keyp:
        print(False)
      else:
        print(True)
        break