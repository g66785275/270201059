def harmonic(n):
  sum = 0
  for a in range(1,n+1):
    sum+= 1/a
  return sum
print(harmonic(5))
def harmonic(n):
  if n==1:
    return 1
  return 1/n + harmonic(n-1)
y=5
print(harmonic(y))