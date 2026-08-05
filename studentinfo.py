roll_no = int(input("Enter Roll Number: "))
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))

mark1 = float(input("Enter Maths Marks: "))
mark2 = float(input("Enter Science Marks: "))
mark3 = float(input("Enter English Marks: "))
mark4 = float(input("Enter social science: "))

total = mark1 + mark2 + mark3  + mark4
percentage = total / 4

if (mark1 >= 40) and (mark2 >= 40) and (mark3 >= 40) and (mark4 >= 40):
    result = "PASS"
else:
    result = "FAIL"

print("\n Student Information")
print("Roll Number :", roll_no)
print("Name        :", name)
print("Age         :", age)

print("\n Marks ")
print("Maths       :", mark1)
print("Science     :", mark2)
print("English     :", mark3)
print("social science :",mark4)

print("\n Result")
print("Total Marks :", total)
print("Percentage  : {:.2f}%".format(percentage))
print("Status      :", result)