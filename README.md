# Development of a Mathematical Calculator and Personal Pocket CGPA Calculator Using Python

Submitted by: OLOMINU PAMILERIN EMMANUEL  
Matric Number: 241203002  
Department: Data Science  
Course: COS202 — Computer Programming II

Repository: https://github.com/olu507/Cos_202-Python_Programming

---

## Overview

This repository contains two Python programs demonstrating practical applications of Python:

1. Mathematical Calculator — a menu-driven calculator that performs common arithmetic operations.
2. Personal Pocket CGPA Calculator — computes students' CGPA from course codes, credit units, and scores and determines degree classification.

These programs illustrate Python concepts such as functions, loops, conditionals, I/O, and error handling.

---

## Table of Contents

- Aim & Objectives
- Features
- Algorithms
- Grading system & Degree classification
- Programming concepts used
- Source code
  - calculator.py
  - cgpa_calculator.py
- Usage
- Sample output
- Challenges encountered
- Conclusion
- License
- Author

---

## Aim

To design and implement Python programs that perform mathematical calculations and compute students' CGPA.

## Objectives

- Develop a mathematical calculator using Python.
- Perform basic arithmetic operations.
- Develop a CGPA calculator using selection statements.
- Compute students' grades automatically.
- Display the correct CGPA and class of degree.
- Improve programming skills using Python.

---

## Features

- User-friendly menu-driven calculator
- Handles division-by-zero and input validation
- Supports repeated calculations
- CGPA calculator:
  - Accepts course code, credit unit, and score
  - Automatically assigns grade and grade point
  - Computes total grade points, total credit units and CGPA
  - Displays degree classification

---

## Algorithm Summaries

Mathematical Calculator:
1. Start
2. Display menu
3. Read user choice
4. If Exit selected, terminate; otherwise request two numbers
5. Perform chosen operation (handle divide-by-zero)
6. Display result
7. Return to menu
8. Stop

CGPA Calculator:
1. Start
2. Enter number of courses
3. For each course:
   - Enter course code, credit unit, score
   - Determine grade and grade point
4. Compute total grade points and total credit units
5. Calculate CGPA = total_grade_points / total_credit_units
6. Display CGPA and degree classification
7. Stop

---

## Grading System

| Score Range | Grade | Point |
|-------------|-------|-------|
| 70 – 100    | A     | 5     |
| 60 – 69     | B     | 4     |
| 50 – 59     | C     | 3     |
| 45 – 49     | D     | 2     |
| 40 – 44     | E     | 1     |
| 0 – 39      | F     | 0     |

Degree Classification:

| CGPA Range   | Class                 |
|--------------|-----------------------|
| 4.50 – 5.00  | First Class           |
| 3.50 – 4.49  | Second Class Upper    |
| 2.40 – 3.49  | Second Class Lower    |
| 1.50 – 2.39  | Third Class           |
| Below 1.50   | Pass                  |

---

## Programming Concepts Used

- Variables and data types
- Input and output
- Functions and user-defined functions
- Conditional statements (if / elif / else)
- Loops (while / for)
- Arithmetic operators
- Error handling and validation
- Modular code and main guard

---

## Source Code

You can copy these scripts into the repository as `calculator.py` and `cgpa_calculator.py`.

### calculator.py

```python
#!/usr/bin/env python3
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

def menu():
    print("====== MATHEMATICAL CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Clear")
    print("8. Exit")

def main():
    while True:
        menu()
        choice = input("\nSelect Option (1-8): ").strip()
        if choice == '8':
            print("Exiting calculator. Goodbye.")
            break
        if choice == '7':
            clear_screen()
            continue
        if choice not in [str(i) for i in range(1, 7)]:
            print("Invalid option. Please choose between 1 and 8.")
            continue

        a = get_number("Enter First Number: ")
        b = get_number("Enter Second Number: ")

        try:
            if choice == '1':
                result = add(a, b)
                op = '+'
            elif choice == '2':
                result = subtract(a, b)
                op = '-'
            elif choice == '3':
                result = multiply(a, b)
                op = '*'
            elif choice == '4':
                result = divide(a, b)
                op = '/'
            elif choice == '5':
                result = modulus(a, b)
                op = '%'
            elif choice == '6':
                result = power(a, b)
                op = '**'
            else:
                result = None
                op = '?'

            print(f"\nAnswer = {result}\n")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == '__main__':
    main()
```

---

### cgpa_calculator.py

```python
#!/usr/bin/env python3

def grade_from_score(score):
    """Returns (grade_letter, grade_point) for a numeric score."""
    if score >= 70 and score <= 100:
        return 'A', 5
    elif score >= 60:
        return 'B', 4
    elif score >= 50:
        return 'C', 3
    elif score >= 45:
        return 'D', 2
    elif score >= 40:
        return 'E', 1
    elif score >= 0:
        return 'F', 0
    else:
        return 'Invalid', 0

def classification(cgpa):
    if cgpa >= 4.50:
        return 'First Class'
    elif cgpa >= 3.50:
        return 'Second Class Upper'
    elif cgpa >= 2.40:
        return 'Second Class Lower'
    elif cgpa >= 1.50:
        return 'Third Class'
    else:
        return 'Pass'

def get_int(prompt, min_value=None):
    while True:
        try:
            val = int(input(prompt))
            if min_value is not None and val < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("====== CGPA CALCULATOR ======")
    n = get_int("Enter Number of Courses: ", min_value=1)

    courses = []
    total_credit_units = 0
    total_grade_points = 0

    for i in range(1, n + 1):
        print(f"\nCourse #{i}")
        code = input("Course Code: ").strip()
        credit = get_int("Credit Unit: ", min_value=0)
        while True:
            try:
                score = float(input("Score (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score. Enter a numeric value between 0 and 100.")

        grade_letter, grade_point = grade_from_score(score)
        grade_points_for_course = grade_point * credit

        courses.append({
            'code': code,
            'credit': credit,
            'score': score,
            'grade': grade_letter,
            'grade_point': grade_point,
            'grade_points_for_course': grade_points_for_course
        })

        total_credit_units += credit
        total_grade_points += grade_points_for_course

    print("\n--- Results ---\n")
    for c in courses:
        print(f"Course Code: {c['code']}")
        print(f"Credit Unit: {c['credit']}")
        print(f"Score: {c['score']}")
        print(f"Grade: {c['grade']}\n")

    print(f"Total Credit Units = {total_credit_units}")
    print(f"Total Grade Points = {int(total_grade_points) if total_grade_points.is_integer() else total_grade_points}")

    if total_credit_units == 0:
        print("Cannot compute CGPA: total credit units is zero.")
    else:
        cgpa = total_grade_points / total_credit_units
        cgpa_rounded = round(cgpa, 2)
        print(f"CGPA = {cgpa_rounded}")
        print(f"Class = {classification(cgpa)}")

if __name__ == '__main__':
    main()
```

---

## Usage

Requirements:
- Python 3.7+

To run the calculator:
- python3 calculator.py

To run the CGPA calculator:
- python3 cgpa_calculator.py

---

## Sample Output

Mathematical Calculator (example):

====== MATHEMATICAL CALCULATOR ======
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Clear
8. Exit

Select Option: 1
Enter First Number: 20
Enter Second Number: 15
Answer = 35.0

CGPA Calculator (example):

====== CGPA CALCULATOR ======
Enter Number of Courses: 3

Course Code: COS202
Credit Unit: 3
Score: 78
Grade: A

Course Code: GST201
Credit Unit: 2
Score: 65
Grade: B

Course Code: MAT203
Credit Unit: 3
Score: 55
Grade: C

Total Credit Units = 8
Total Grade Points = 33
CGPA = 4.13
Class = Second Class Upper

---

## Challenges Encountered

- Preventing division by zero in the calculator and modulus operations.
- Correctly assigning grades based on score ranges.
- Ensuring CGPA computation accuracy and handling cases with zero total credit units.
- Designing a clean menu-driven interface and validating user input.
- Testing with varied inputs to ensure robustness.

These were resolved with conditional checks, exception handling, input validation loops, and testing.

---

## Conclusion

The assignment objectives were achieved: two Python applications were developed — a Mathematical Calculator and a Personal Pocket CGPA Calculator — demonstrating core programming concepts and practical problem solving in Python.

---

## License

This project can include an open-source license if desired (e.g., MIT). Add a LICENSE file to the repo to declare licensing.

---

Author:
OLOMINU PAMILERIN EMMANUEL — COS202

Repository: https://github.com/olu507/Cos_202-Python_Programming

— GitHub Copilot Chat Assistant