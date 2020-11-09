
giriş = input("Number:")
if len(giriş)>1:
  print("Two last digits:",giriş[-2:])
elif len(giriş) == 1:
  print("Two last digits:","0",giriş)