"""
    car_go.py
    Jessica Soler
    4/7/24
    Car Class for car_go.py file
"""
import car

def main():
    
    my_car = car.Car()
    

    my_car.set_color()
    my_car.set_speed()

    
    #TODO: get input: what color is your car
    print(f"The car color is: {my_car.get_color()}")
    print(f"The car speed is: {my_car.get_speed()}")

    while True:
        choice = input("(a)ccelerate, (b)rake, or (e)xit: ")
        if choice == "a":
            my_car.accelerate()
        elif choice == "b":
            my_car.brake()
        elif choice == "e":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select (a) to , (b), or (e).")

main()