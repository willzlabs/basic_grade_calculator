def score_input(subject: str) -> int:

    """This function collects the score of a subject"""
    
    while True:

            try:
                print()
                score = int(input(f"Enter {subject} score: "))
                if score < 0 or score > 100:
                    raise ValueError("Score can only be between the ranges of 0 - 100! Try again.")
                return score
            except ValueError as e:
                if str(e) == "Score can only be between the ranges of 0 - 100! Try again.":
                    print("Score can only be between the ranges of 0 - 100! Try again.")
                else:
                    print("Invalid input! Enter a valid score.")