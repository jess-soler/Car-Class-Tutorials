"""
    car.py
    Jessica Soler
    4/7/24
    Car Class for car_go.py file
"""


#TODO: create a class for car
class Car:
    
    #attributes: color && speed
    #initialize in __init__
    # def __init__(self):
    #     self.color = color
    #     self.speed = speed
        
         
        #Methods: accelerate() brake() get_speed() get_color()
    def set_color(self):
        self.color = str(input("What color is your car?: "))

    def get_color(self):
        return self.color
        
    def set_speed(self):
        self.speed = int(input("How fast do you want to drive?: "))
            
    def get_speed(self):
        return self.speed
    
    def accelerate(self):
        self.speed = self.speed + 5
        print(f"Your car is now going {self.speed} mph.")

    def brake(self):
        self.speed = self.speed - 5
        print(f"Your car is now going {self.speed} mph.")
