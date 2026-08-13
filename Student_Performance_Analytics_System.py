import csv

subjects = ["Maths", "Science", "English", "Computer", "Gujarati"]

students = []
all_names = []
percentages = []

grade_students = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        roll_no = int(row["Roll No"])
        name = row["Name"]

        marks = [
            int(row["Maths"]),
            int(row["Science"]),
            int(row["English"]),
            int(row["Computer"]),
            int(row["Gujarati"])
        ]

        marks_tuple = tuple(marks)

        total = sum(marks)
        percentage = total / 5

        if percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        student = {
            "Roll No": roll_no,
            "Name": name,
            "Marks": marks_tuple,
            "Total": total,
            "Percentage": percentage,
            "Grade": grade
        }

        students.append(student)
        all_names.append(name)
        percentages.append(percentage)
        grade_students[grade].append(name)

class_average = sum(percentages) / len(percentages)

highest = max(percentages)
lowest = min(percentages)

highest_scorers = []
lowest_scorers = []

for student in students:

    if student["Percentage"] == highest:
        highest_scorers.append(student["Name"])

    if student["Percentage"] == lowest:
        lowest_scorers.append(student["Name"])

above_average = []

for student in students:

    if student["Percentage"] > class_average:
        above_average.append(student["Name"])

failed_students = []

for student in students:

    for mark in student["Marks"]:

        if mark < 40:
            failed_students.append(student["Name"])
            break

print("\n========== STUDENT PERFORMANCE REPORT ==========")

for student in students:

    print("\nRoll No   :", student["Roll No"])
    print("Name      :", student["Name"])
    print("Marks     :", student["Marks"])
    print("Total     :", student["Total"])
    print("Percentage:", student["Percentage"])
    print("Grade     :", student["Grade"])

print("\nClass Average:", class_average)

print("\nHighest Scorer(s):")
for name in highest_scorers:
    print(name, "-", highest, "%")

print("\nLowest Scorer(s):")
for name in lowest_scorers:
    print(name, "-", lowest, "%")

print("\nStudents Above Class Average:")
for name in above_average:
    print(name)

print("\nStudents Failed in One or More Subjects:")
for name in failed_students:
    print(name)

print("\nStudents According to Grade:")

for grade in grade_students:
    print(grade, ":", grade_students[grade])

alphabetical_names = sorted(all_names)

print("\nAlphabetical Order:")

for name in alphabetical_names:
    print(name)

highest_score = -1
second_highest_score = -1

for percentage in percentages:

    if percentage > highest_score:
        second_highest_score = highest_score
        highest_score = percentage

    elif percentage > second_highest_score and percentage != highest_score:
        second_highest_score = percentage

print("\nSecond Highest Scorer:")

for student in students:

    if student["Percentage"] == second_highest_score:
        print(student["Name"], "-", second_highest_score, "%")

subject_averages = {}

for i in range(5):

    total = 0

    for student in students:
        total = total + student["Marks"][i]

    subject_averages[subjects[i]] = total / len(students)

highest_subject_average = max(subject_averages.values())

print("\nSubject Averages:")

for subject in subject_averages:
    print(subject, ":", subject_averages[subject])

print("\nHighest Average Subject:")

for subject in subject_averages:

    if subject_averages[subject] == highest_subject_average:
        print(subject, "-", highest_subject_average)

name_set = set()
duplicate_names = []

for name in all_names:

    if name in name_set:

        if name not in duplicate_names:
            duplicate_names.append(name)

    else:
        name_set.add(name)

print("\nDuplicate Names:")

if len(duplicate_names) == 0:
    print("No duplicate names found.")
else:
    for name in duplicate_names:
        print(name)