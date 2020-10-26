gpa = float(input("Gpa:"))
number_of_lectures = int(input("Number Of Lectures:"))

if gpa < 2  and number_of_lectures <47:
  print("Not enough gpa and number of lectures!")
elif gpa >= 2  and number_of_lectures <47:
  print("Not enough  number of lectures!")
elif gpa < 2  and number_of_lectures >=47:
  print("Not enough gpa !")
else:
  print("GRADUATED!")