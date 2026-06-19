from banner import banner
from menu import menu
from name_input import name_input
from score_input import score_input
from grade_calculator import grade_calculator
from recalc_opt import recalc_opt

def main() -> None:

    """This is the main function of the basic grade calculator program"""

    banner()

    active = True

    while active:

        choice = menu()

        if choice == 1:

            name = name_input()

            math = score_input("math")

            english = score_input("english")

            science = score_input("science")
                
            print()

            result = grade_calculator(name, math, english, science)

            print("-------------------------------")
            print(result)
            print("-------------------------------")
            print()
            
            calc_again = recalc_opt()

            if calc_again == 2:
                active = False
                print("Thank you for using Student Grade Calculator. See you next time!")
                print("----------------------------------------------------------------")
                print()
            else:
                print("----------------------------")
    
        else:

            active = False
            print("Thank you for using Student Grade Calculator. See you next time!")
            print("----------------------------------------------------------------")
            print()

if __name__ == "__main__":
    main()