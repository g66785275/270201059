notlar = []
while True: 
  giriş = input("Notu girin:(q çıkış)")
  if giriş == "q":
    break
  if int(giriş) > 90:
    notlar.append(giriş)
print(notlar)