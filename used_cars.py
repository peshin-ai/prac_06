"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("limo", 100)
    # print('{}'.format(limo.name))
    limo.add_fuel(20)
    print("the amount of fuel in the car is {}".format(limo.fuel))
    limo.drive(115)
    print(" the car's odometer reading is {}".format(limo.odometer))
    # limo.__str__()


if __name__ == '__main__':
    main()
