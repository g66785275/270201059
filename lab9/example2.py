def reversed(liste):
  if len(liste) ==0:
    return []
  return [liste.pop()]+reversed(liste)
print(reversed([1,2,3,4]))