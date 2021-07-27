# What do  you understand by __init__ method in python.
""" Ans.
1.  ___init__  is special method in python. It is a constructor method for a class in python.
2.  __init__ is called when ever an object of the class is constructed.
3.  __init__ method in python which is used to initilze the variable in a class.

"""

class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def print_student(self):
        print("Name:-  ", self.name)
        print("Age:-  ", self.age)
        print("Branch:-  ", self.branch)

student1 = Student("Sunil Kumar Maurya", 25, "MCA")
student1.print_student()
