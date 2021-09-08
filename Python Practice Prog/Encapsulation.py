# Encapsulation in python
class Encap():
	def __init__(self):
		self.name = "Sunil Kumar Maurya"
		self.__age = "25"
	def Student(self):
		return self.name + self.__age
ob = Encap()
print(ob.name)
# This showing error due to Encapsulation
print(ob.__age)
# For calling this encapsulated item outside the class.
#print(ob._Encap__age)
print(ob.Student())
