class Car:
    car_type = 'sports'
    def __init__(self,color):
        self.__color=color
    def print_car(self):
        print(self.__color,"\t", self.car_type)
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color=color


car2=Car("yellow")
car2.print_car()
car2.color="black"

