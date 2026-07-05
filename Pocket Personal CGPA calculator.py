# ==========================================
# COS202 PERSONAL POCKET CGPA CALCULATOR
# Name: Abass Nurudeen
# Matric No: 241203039
# Department: Data Science
# ==========================================

def grade_point(grade):
    grade = grade.upper()

    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        return None


print("=" * 45)
print("     PERSONAL POCKET CGPA CALCULATOR")
print("=" * 45)

while True:
    try:
        total_courses = int(input("\nEnter the number of courses: "))

        total_grade_points = 0
        total_credit_units = 0

        for i in range(1, total_courses + 1):
            print(f"\nCourse {i}")

            course = input("Course Code: ")

            credit = int(input("Credit Unit: "))

            while True:
                grade = input("Grade (A-F): ").upper()

                point = grade_point(grade)

                if point is not None:
                    break
                else:
                    print("Invalid grade! Enter A, B, C, D, E or F.")

            total_grade_points += point * credit
            total_credit_units += credit

        gpa = total_grade_points / total_credit_units

        print("\n" + "=" * 45)
        print(f"Total Credit Units : {total_credit_units}")
        print(f"Total Grade Points : {total_grade_points}")
        print(f"Your GPA/CGPA is   : {gpa:.2f}")
        print("=" * 45)

    except ValueError:
        print("Please enter valid numbers only.")
        continue

    choice = input("\nCalculate again? (Y/N): ").upper()

    if choice != "Y":
        print("\nThank you for using the Personal Pocket CGPA Calculator.")
        break