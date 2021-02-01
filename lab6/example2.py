grade = [[50,90,60],[15,60,75],[99,95,91]]
indexim = 0
num = 0
for a in grade:
  one = grade[0][0]*(0.3)+grade[0][1]*(0.3)+grade[0][2]*(0.4)
  two = grade[1][0]*(0.3)+grade[1][1]*(0.3)+grade[1][2]*(0.4)
  three = grade[2][0]*(0.3)+grade[2][1]*(0.3)+grade[2][2]*(0.4)
  grade.append([one,two,three])