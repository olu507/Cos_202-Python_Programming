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
Score: 89
Grade: A

Course Code: GST201
Credit Unit: 2
Score: 65
Grade: B

Course Code: MAT202
Credit Unit: 2
Score: 66
Grade: B

Total Credit Units = 7
Total Grade Points = 33
CGPA = 4.71
Class = First Class Upper


## Challenges Encountered

- Preventing division by zero in the calculator and modulus operations.
- Correctly assigning grades based on score ranges.
- Ensuring CGPA computation accuracy and handling cases with zero total credit units.
- Designing a clean menu-driven interface and validating user input.
- Testing with varied inputs to ensure robustness.

These were resolved with conditional checks, exception handling, input validation loops, and testing.


## Conclusion

The assignment objectives were achieved: two Python applications were developed a Mathematical Calculator and a Personal Pocket CGPA Calculator demonstrating core programming concepts and practical problem solving in Python.


Author:
OLOMINU PAMILERIN EMMANUEL — COS202

Repository: https://github.com/olu507/Cos_202-Python_Programming

— GitHub Copilot Chat Assistant