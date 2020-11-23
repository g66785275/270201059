a =input("Please enter your name:")
c = ''
for q in a:
  print(q.upper())
while True:
  b = input("Please enter any string ('quit'to quit):")

  if b == "quit":
    print(c)
    break
  else:
    c += b
