from guitar import guitars

Array = []


def main():
    print("My guitars!")
    print("To open list, enter nothing in the name")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        Adding_new_item = guitars(name, year, cost)
        Array.append(Adding_new_item)
        print(" {} ({}): ${} added.".format(Adding_new_item.name, Adding_new_item.year, Adding_new_item.cost))
        name = input("Name: ")
    if Array:
        Array.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(Array):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1:>5} ({2}), worth ${3:2,.2f} {4}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print("No guitars")


main()
