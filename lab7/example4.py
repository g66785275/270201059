a = 0
salary_list = []
employees = dict()
while a <5:
  employee = input("Name:")
  salary = int(input("Salary:"))
  employees[salary] = employee
  salary_list.append(salary)
  a += 1
salary_list.sort()
for a in salary_list[-3:]:
  print(employees[a])
