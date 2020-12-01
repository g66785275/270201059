
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
a = dict()
for q in books:
  length = len(q)
  for w in q:
    if q.count(w)>1:
      length1 = length - q.count(w)+1
  a[q] = (length,length1)
for a,b in a.items():
  print("{}-->{}".format(a,b))