password = "abc123"

index = 0
while True:
  entry = input("Password: ")

  if entry == "help" :
    print(password[index])
    index += 1 
  elif entry == password:
    print("Welcome ! ")
    break
  elif entry != password:
    print("Wrong")    