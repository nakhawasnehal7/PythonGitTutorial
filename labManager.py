# Auther SnehalNakhawa
# Date 24th February 2026
# Description - This program manages a laboratory inventory system
# allowing users to add remove and display equipments


lab_equipment = []

print("Welcome to the inventory manager for your laboratory!\n")

while True:
    print("\n You can choose from the following options:")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")

    choice = input("What would you like to do:")

    if choice == "1":
        if len(lab_equipment) >= 7:
            print("Your Laboratory cannot support any more equipment!")
        else:
            item = input("What would you like to add to the Laboratory:")
            lab_equipment.append(item)
            print(f"{item} has been added")
    elif choice == "2":
        item = input("What would you like to remove from the Laboratory :")
        if item in lab_equipment:
            lab_equipment.remove(item)
            print(f"{item} has been removed")
        else:
            print(f"{item} was not present and could not be removed")
    elif choice == "3":
        print("Your Laboratory currently contains:", end="")
        for item in lab_equipment:
            print(item, end=" ")

        print()

    elif choice == "4":
        print("Good luck on your journey of discovery!")
        break

    else:
        print(f"{choice} was not a valid option. Please try again")
