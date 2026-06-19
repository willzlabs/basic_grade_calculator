def grade_calculator(student_name: str, math_score: int, english_score: int, science_score: int, passing_mark: int = 40) -> str:

    """This function calculates a student's final grade and determines whether they passed or failed"""

    student_score = (math_score + english_score + science_score) / 3
    student_score = round(student_score, 2)

    if student_score < passing_mark:
        return f"Student  : {student_name}\n" f"Average  : {student_score}\n" f"Status   : FAILED ❌"
    else:
        return f"Student  : {student_name}\n" f"Average  : {student_score}\n" f"Status   : PASSED ✅"