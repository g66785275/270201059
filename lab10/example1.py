def three(n):
  if n == 0:
    return 0
  else:
    return 3+three(n-1)

print(three(3))