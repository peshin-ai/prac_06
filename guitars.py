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
        print("{} ({}): ${.2f} added.".format(Adding_new_item.name, Adding_new_item.year, Adding_new_item.cost))
        name = input("Name: ")
    if Array:
        print("These are my guitars:")
        for i, guitar in enumerate(Array):
            text_vintage = ""
            if guitar.is_vintage():
                text_vintage = "(vintage)"
            print("Guitar {0}: {1} ({2}), worth ${3:,.2f} {4}".format(i + 1, guitar.name, guitar.year, guitar.cost, text_vintage))
    else:
        print("No guitars")


main()
