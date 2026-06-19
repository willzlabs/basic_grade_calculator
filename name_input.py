def name_input() -> str:

    """This function collects the name of a student"""

    while True:

        try:
            name = ' '.join(input("Enter student name: ").split())
            if name == "":
                raise ValueError("Name cannot be empty. Try again!")
            elif not name.replace(' ', '').replace('-', '').replace('\'', '').isalpha():
                raise ValueError("Name must contain letters only. Try again!")
            return name
        except ValueError as e:
            if str(e) == "Name cannot be empty. Try again!":
                print("Name cannot be empty. Try again!")
                print()
            elif str(e) == "Name must contain letters only. Try again!":
                print("Name must contain letters only. Try again!")
                print()