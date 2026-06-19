def menu() -> int:

    """This function displays a menu and enables selection of options within the menu"""

    while True:

            try:
                print()
                print("1. Calculate student's grade")
                print("2. Exit")
                print()
                choice = int(input("Select an option: "))
                print()
                if choice not in (1, 2):
                    raise ValueError("Invalid input! Select either option 1 or 2.")
                return choice
            except ValueError as e:
                if str(e) == "Invalid input! Select either option 1 or 2.":
                    print("Invalid input! Select either option 1 or 2.")
                    print("\n----------------------------")
                else:
                    print()
                    print("Invalid input! Select an option between 1 and 2.")
                    print("\n----------------------------")