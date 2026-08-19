# Empty Lists
marks = []
names = []

for i in range(10):
    name = input("Enter student name: ")
    mark = int(input("Enter student marks: "))

    names.append(name)
    marks.append(mark)

marks_tuple = tuple(marks)

student = dict(zip(names, marks))

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\nStudents scoring above average:")

for name in student:
    if student[name] > average:
        print(name, ":", student[name])

unique_marks = set(marks)

print("\n========== Student Marks Analysis ==========")
print("Marks List         :", marks)
print("Marks Tuple        :", marks_tuple)
print("Student Dictionary :", student)
print("Highest Marks      :", highest)
print("Lowest Marks       :", lowest)
print("Average Marks      :", average)
print("Unique Marks       :", unique_marks)