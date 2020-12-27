def evens(liste):
  count =0
  if len(liste) == 0:
    return count
  else:
    if liste[0] % 2 == 0:
      count=1
    return count + evens(liste[1:])
print(evens([0,1,2,3,4,5,6]))