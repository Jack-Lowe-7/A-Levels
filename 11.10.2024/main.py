"""
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


class Person:
  #runs every time the claass is initaiated
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""

class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

class staff(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    