# Inheritance using super class(Single Inheritance)
class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("\n ** I'am Vehicle ** ")
        print("Mileage of the Vehicle:-  ", self.mileage)
        print("Cost of the Vehicle:-  ", self.cost)

class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_detail(self):
        print("\n ** I'am Car ** ")
        print("Number of tyres in car:-  ", self.tyres)
        print("Horse-Power of car is:-  ", self.hp)

c1 = Car(600, 500000, 4, 800)
c1.show_car_detail()
c1.show_vehicle_details()