grades = []
count_above_90 = 0
sum_grades = 0

num_grades = int(input("how many grades do you want? "))

for i in range(num_grades):
    try:
        grade = float(input(f"Enter a grade {i + 1}: "))

        if grade < 0 or grade > 100:
            print("invlid grade")
            continue

        grades.append(grade)
        sum_grades += grade

        if grade > 90:
            count_above_90 += 1

    except ValueError:
        print("Not a number, try again")
        continue

if grades:
    max_grade = max(grades)
    min_grade = min(grades)
    average = sum_grades / len(grades)

    print("Highest grade", max_grade)
    print("Number of valid grades", len(grades))
    print("grades above 90:", count_above_90)
    print("Class Average", average)
else:
    print("invalid grade")








