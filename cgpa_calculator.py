# COS202 Personal Pocket CGPA Calculator

print("====== CGPA CALCULATOR ======")

total_credit_units = 0
total_grade_points = 0

num_courses = int(input("Enter number of courses: "))

for i in range(num_courses):
    print(f"\nCourse {i+1}")

    course = input("Course Code: ")
    credit = int(input("Credit Unit: "))
    score = float(input("Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    gp = point * credit

    total_credit_units += credit
    total_grade_points += gp

    print("Grade:", grade)
    print("Grade Point:", gp)

cgpa = total_grade_points / total_credit_units

print("\n========== RESULT ==========")
print("Total Credit Units:", total_credit_units)
print("Total Grade Points:", total_grade_points)
print("CGPA =", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")
elif cgpa >= 3.50:
    print("Class: Second Class Upper")
elif cgpa >= 2.40:
    print("Class: Second Class Lower")
elif cgpa >= 1.50:
    print("Class: Third Class")
else:
    print("Class: Pass")