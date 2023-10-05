class Employee:
  def __init__(self,name,age,gender,salary):
    if salary <= 0:
      print('salary cannot be a zero amount')
  #   else:
  #      self.salary = salary
    self.name = name,
    self.age = age,
    self.gender = gender,
    self.salary = salary,
  def __str__(self):
    return f'name:{self.name}\nage:{self.age}\ngender:{self.gender}\nsalary:{self.salary}'
employee1 = Employee(
  str(input('enter employee name:')),
  int(input('enter employee age:')),
  str(input('enter employee gender:')),
  int(input('enter employee salary:')),
)
print(employee1)
