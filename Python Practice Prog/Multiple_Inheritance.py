"""
In Multiple inheritance the child inherits more then 1 parent class.

"""
class Parent1:
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2:
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2

class Child(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3

my_Child = Child()
my_Child.assign_string_one("I am String of Parent1 ")
my_Child.assign_string_two("I am String of Parent2 ")
my_Child.assign_string_three("I am String of Child")
my_Child.show_string_one()
my_Child.show_string_two()
my_Child.show_string_three()