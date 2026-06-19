def recalc_opt() -> int:

    """This function gives the user an option to calculate again or not"""

    while True:

        try:
            calc_again = int(input("Do you want to calculate again?\n\n1. Yes\n2. No\n\nSelect an option: "))
            print()
            if calc_again not in (1, 2):
                raise ValueError("Enter either 1 or 2!")
            return calc_again
        except ValueError as e:
            if str(e) == "Enter either 1 or 2!":
                print("Enter either 1 or 2!")
                print()
                print("-------------------------------\n")
            else:
                print("Enter either 1 for Yes or 2 for No!")
                print()
                print("-------------------------------\n")