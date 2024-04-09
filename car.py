"""
    car.py
    Jessica Soler
    4/7/24
    Car Class for car_go.py file
"""
# def main():
#     pass

#TODO: create a class for car
class Car():
    #attributes: _color && _speed
    #initialize in __init__
    def __init__(self):
        # self._color
        # self._speed
      
        #Methods: accelerate() brake() get_speed() get_color()
        def accelerate(self):
            self._speed = self._speed + 5
    
        def brake(self):
            self._speed = self._speed - 5
    
        def get_speed(self):
            self._speed = 55
            
        def get_color(self):
            self._color = str(input("What color is your car?: "))
            print(f"The car is {self._color}")
    
        

# if __name__ == "__main__":
#     main()