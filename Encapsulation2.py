class Iqburn():
    def __init__(self):
        self.course = "Django is a Web development Course"
        self.__tech = "Django"

    def Course(self):
        return self.course + ":" + self.__tech

    def set__tech(self, x):
        self.__tech = x

    def get__tech(self):
        return self.__tech

ob=Iqburn
ob.set__tech("Python")
ob.Course()
ob.get__tech()