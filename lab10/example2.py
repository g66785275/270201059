def hailstone(x):
  a = ""
  if x ==1:
    return "1"
  else:
    if x%2==0:
     return str(int(x/2)) +"  "+hailstone(x/2)
    else:
      return  str(3*x+1) +" " +hailstone(3*x+1)

print(hailstone(5))