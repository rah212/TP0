grades = []
names = []

for _ in range(10):
    name = input("Enter the student's name: ")
    grade = float(input(f"Enter the grade for {name}: "))
    names.append(name)                                                                                                                                  
    grades.append(grade)

average = sum(grades) / len(grades)
best_student_index = grades.index(max(grades))
best_student = names[best_student_index]

print(f"The average grade is: {average:.2f}")
print(f"The best student is: {best_student} with a grade of {grades[best_student_index]}")