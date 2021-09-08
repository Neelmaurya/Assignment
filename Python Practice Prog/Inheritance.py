"""
What do you understand by Inheritance in python.
Ans:-
Inheritance refers to the properties one class acquiring the property of another class.

"""

class Fruit:
    def __init__(self):
        print("I am a Fruit")

class Citrus(Fruit):
    def __init__(self):
        super().__init__()
        print("I am Citrus")

Lemon = Citrus()