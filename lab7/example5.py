
k = 0
while True:

  keyp=input()
  if len(keyp) < 8:
    print(False)
  else:
    for q in keyp:
      if q != int(q):
        k+=1
    if k == len(keyp):
        print(False)
    if keyp.lower() == keyp:
      print(False)
    else:
      if keyp.upper() == keyp:
        print(False)
      else:
        print(True)
        break