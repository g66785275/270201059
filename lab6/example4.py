liste = [int(i) for i in input("Listenizi Yazınız:").split()]
liste2 = []
for a in liste:
  if a not in liste2:
    liste2.append(a)
liste2.sort()
liste2.reverse()
print(liste2)
