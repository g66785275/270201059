def add(x,y,z):
  return x+y+z
def multiply(x,y):
  return x*y

def f(a,b):
  a2 = multiply(a,a)
  a3 = multiply(a2,a)
  ab = multiply(a,b)
  result = add(a3,ab,b)
  return result
print(f(2,3))
