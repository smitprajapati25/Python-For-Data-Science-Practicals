import numpy as np

batch = input("Enter Batch Information: ").strip()

batch_parts = batch.split("-")
department = "-".join(batch_parts[2:])

subjects = ("Maths", "Science", "English", "Computer", "Gujarati")

names = []

for i in range(10):
    name = input("Enter Student " + str(i + 1) + " Name: ")
    names.append(name)

roll_numbers = range(1, 11)

marks = []

for i in range(10):

    print("\nEnter marks for", names[i])

    student_marks = []

    for subject in subjects:
        mark = int(input("Enter " + subject + " Marks: "))
        student_marks.append(mark)

    marks.append(student_marks)

marks_array = np.array(marks)

total_marks = np.sum(marks_array, axis=1)

percentage = total_marks / 5

subject_average = np.mean(marks_array, axis=0)

highest_marks = np.max(marks_array)
lowest_marks = np.min(marks_array)

highest_student_index = np.argmax(total_marks)
lowest_student_index = np.argmin(total_marks)

highest_student = names[highest_student_index]
lowest_student = names[lowest_student_index]

overall_average = np.mean(percentage)

highest_subject_index = np.argmax(subject_average)
lowest_subject_index = np.argmin(subject_average)

highest_subject = subjects[highest_subject_index]
lowest_subject = subjects[lowest_subject_index]

print("\nMarks of First Three Students in Last Two Subjects:")
print(marks_array[:3, -2:])

search_subject = input("\nEnter subject to search: ")

search_subject = search_subject.strip().lower()

found = False

for i in range(len(subjects)):
    if subjects[i].lower() == search_subject:
        print(subjects[i], "is present at index", i)
        found = True
        break

if found == False:
    print("Subject is not present in the subject tuple.")

distinction_students = []

for i in range(10):
    if percentage[i] >= 85:
        distinction_students.append(names[i])

failed_students = []

for i in range(10):
    if np.any(marks_array[i] < 40):
        failed_students.append(names[i])

above_average_students = []

for i in range(10):
    if percentage[i] > overall_average:
        above_average_students.append(names[i])

reverse_names = names[::-1]

alphabetical_names = sorted(names)

print("\n========== STUDENT PERFORMANCE ==========")

for i in range(10):

    print("\nRoll No   :", roll_numbers[i])
    print("Name      :", names[i])
    print("Marks     :", marks_array[i])
    print("Total     :", total_marks[i])
    print("Percentage:", percentage[i])

print("\n========== SUBJECT AVERAGES ==========")

for i in range(5):
    print(subjects[i], ":", subject_average[i])

print("\nHighest Marks in Class:", highest_marks)
print("Lowest Marks in Class:", lowest_marks)

print("\nHighest Scoring Student:")
print(highest_student, "-", total_marks[highest_student_index])

print("\nLowest Scoring Student:")
print(lowest_student, "-", total_marks[lowest_student_index])

print("\nOverall Class Average Percentage:", round(overall_average, 2))

print("\nSubject with Highest Average:")
print(highest_subject, "-", subject_average[highest_subject_index])

print("\nSubject with Lowest Average:")
print(lowest_subject, "-", subject_average[lowest_subject_index])

print("\nDistinction Students:")
print(distinction_students)

print("\nStudents Failed in One or More Subjects:")
print(failed_students)

print("\nStudents Above Class Average:")
print(above_average_students)

print("\nStudent Names in Reverse Order:")
print(reverse_names)

print("\nStudent Names in Alphabetical Order:")
print(alphabetical_names)

print("\n========== FINAL ACADEMIC REPORT ==========")

print("Batch Name                 :", batch)
print("Department Name            :", department)
print("Total Number of Students  :", len(names))
print("Overall Class Average     :", round(overall_average, 2), "%")
print("Highest Scoring Student   :", highest_student)
print("Lowest Scoring Student    :", lowest_student)
print("Highest Average Subject   :", highest_subject)
print("Lowest Average Subject    :", lowest_subject)
print("Number of Distinction     :", len(distinction_students))
print("Number of Failed Students :", len(failed_students))