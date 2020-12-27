import time

def thetime(t):
  if t == 0:
   return 0
  else:  
    print(t)
    time.sleep(1)
    return thetime(t-1) 


print(thetime(5))