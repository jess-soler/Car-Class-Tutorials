"""
    car_go.py
    Jessica Soler
    4/7/24
    Car Class for car_go.py file
"""
import car

def main():
    
    my_car = car.car()
    #Class attributes: self, _color, _speed
    #Class methods: accelerate() brake() get_speed() get_color()

    #TODO: get input: what color is your car
    car_color = my_car.get_color()
    print(f"The car color is: {car_color}")

#TODO: output the blue car is going 50 mph

#TODO: get input: (a)ccellerate or (b)rake: a
#TODO: output: the blue car is going 60 mph

#TODO: get input: (a)ccellerate or (b)rake or (e)xit: b
#TODO: output: the blue car is going 55 mph

#TODO: get input: (a)ccellerate or (b)rake or (e)xit: b
#TODO: output: the blue car is going 50 mph

#TODO: get input: (a)ccellerate or (b)rake or (e)xit: e
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
#             print("Invalid choice. Please select (a), (b), or (e).")
            
if __name__ == "__main__":
    main()