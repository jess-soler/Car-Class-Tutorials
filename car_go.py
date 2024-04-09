"""
    car_go.py
    Jessica Soler
    4/7/24
    Car Class for car_go.py file
"""
import car

def main():
    
    my_car = car.Car()
    # my_car.set_color()
    my_car.set_speed(55)
    speed = my_car.get_speed()
    print(f"The car is going {speed} mph")
    # my_car.get_color()
    # my_car.get_speed()
    
    # #Class attributes: self, _color, _speed
    # #Class methods: accelerate() brake() get_speed() get_color()

    # #TODO: get input: what color is your car
    # print(f"The car color is: {my_car.color}")
    # print(f"The car speed is: {my_car.speed}")

#TODO: output the blue car is going 50 mph

#TODO: get input: (a)ccelerate or (b)rake: a
#TODO: output: the blue car is going 60 mph

#TODO: get input: (a)ccelerate or (b)rake or (e)xit: b
#TODO: output: the blue car is going 55 mph

#TODO: get input: (a)ccelerate or (b)rake or (e)xit: b
#TODO: output: the blue car is going 50 mph

#TODO: get input: (a)ccelerate or (b)rake or (e)xit: e



#  while True:
#         choice = input("(a)ccelerate, (b)rake, or (e)xit: ")
#         if choice == "a":
#             # TODO: Implement acceleration logic
#             pass
#         elif choice == "b":
#             # TODO: Implement braking logic
#             pass
#         elif choice == "e":
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please select (a) to , (b), or (e).")

main()