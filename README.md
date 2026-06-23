# Student Grade Calculator

A simple command-line application that calculates a student's average grade across three subjects and determines their pass/fail status.

---

## Features

- Calculates the average score across **Math**, **English**, and **Science**
- Determines **pass or fail** status based on a configurable passing mark (default: 40)
- Input validation for both student names and subject scores
- Loop-based menu allowing multiple calculations in a single session
- Clean, modular architecture with each concern in its own module

---

## Project Structure

```
student-grade-calculator/
├── main.py               # Entry point — orchestrates the program flow
├── banner.py             # Displays the program banner
├── menu.py               # Main menu with option selection
├── name_input.py         # Student name collection and validation
├── score_input.py        # Subject score collection and validation
├── grade_calculator.py   # Core grade calculation logic
├── recalc_opt.py         # Prompts the user to calculate again or exit
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Requirements

- **Python 3.6+**
- No external libraries — this project uses the Python standard library only.

---

## How to Run

1. **Clone or download** the project files into a folder.

2. **Navigate** to the project directory:
   ```bash
   cd student-grade-calculator
   ```

3. **Run** the program:
   ```bash
   python main.py
   ```

---

## Usage

Once the program starts, you will see the main menu:

```
------------------------
STUDENT GRADE CALCULATOR
------------------------

1. Calculate student's grade
2. Exit

Select an option:
```

Select **1** to begin. You will be prompted to enter:

- The student's name
- A score (0–100) for Math
- A score (0–100) for English
- A score (0–100) for Science

The program then displays the result:

```
-------------------------------
Student  : John Doe
Average  : 72.33
Status   : PASSED ✅
-------------------------------
```

After each calculation, you can choose to calculate again or exit.

---

## Input Validation

| Input        | Rules                                                                 |
|--------------|-----------------------------------------------------------------------|
| Student Name | Letters, spaces, hyphens, and apostrophes only. Cannot be empty.     |
| Subject Score| Integer between 0 and 100 (inclusive).                               |
| Menu Options | Must be either 1 or 2.                                               |

---

## Configuration

The passing mark defaults to **40** and can be adjusted by passing a custom value to `grade_calculator()`:

```python
result = grade_calculator(name, math, english, science, passing_mark=50)
```
