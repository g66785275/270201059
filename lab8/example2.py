def is_prime(a):
  e = 0
  if a<2:
    return False
  for q in range(2,a):
    if a % q == 0:
      e+=1
  if e >0:
    return False
  else:
    return True

def is_prime_between(q,w):
  for a in range(min(q,w)+1,max(q,w)):
    if is_prime(a) == True  :
      print(a)
    else:
      continue
is_prime_between(6,10)
