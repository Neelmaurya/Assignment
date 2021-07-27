# Classes are nothing but it is blueprint and from this blueprint we will create set of objects
# which is related with real world entities

# Create a simple class name Human which would give name and age of person

class Human:
    name = None
    age = None

    def get_name(self):
        print("Enter your name:-  ")
        self.name = input()

    def get_age(self):
        print("Enter your Age:-   ")
        self.age = input()

    def put_name(self):
        print("Your name is  ", self.name)

    def put_age(self):
        print("Your age is   ", self.age)

person1 = Human()
person1.get_name()
person1.get_age()
person1.put_name()
person1.put_age()