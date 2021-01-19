def selection(liste):
  for element in liste:
    if element<liste[liste.index(element)+1]:
      a = element
      b = liste.index(element)
      liste.remove(element)
      liste.insert(a,b)
    else:
      selection(liste[liste.index(element):])
  return liste
selection([1,4,5,2])

def selection_sort(lst):
  n = len(lst)
  for bottom in range(n-1):
    mp = bottom
    for i in range(bottom+1,n):
      if lst[i]<lst[mp]:
        mp+=1
    lst[n],lst[mp]=lst[mp],lst[n]
  return lst