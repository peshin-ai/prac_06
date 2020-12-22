from guitar import guitars

This_year = 2020
Vintage_age = 100

def testing():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = guitars(name, year, cost)
    another = guitars("Another Guitar", 2013, 50)
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name, 7, another.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another.name, False, another.is_vintage()))

if __name__ == '__main__':
    testing()
