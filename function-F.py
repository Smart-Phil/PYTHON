''' A program that:
Take the following input from user:
 1. Number of classes held
 2. Number of classes attended
 Print the percentage of attendance and his/her eligibility. Eg if number of classes held = 10 and the student attended 8 classes. Print ‘Your percentage attendance is 80%, you are
eligible’. if number of classes held = 10 and the student attended 6 times. Print ‘Your
percentage attendance is 60%, you are Ineligible’. '''



# Accept input from the user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Check eligibility based on attendance percentage
if attendance_percentage >= 75:
    print(f"Your percentage attendance is {attendance_percentage}%, you are eligible.")
else:
    print(f"Your percentage attendance is {attendance_percentage}%, you are ineligible.")

