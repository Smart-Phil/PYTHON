'''  Write a program that accepts two inputs from a user. Print the greater number or print ‘The 
numbers are equal’. E.g if entered value is 4 and 7, print 7. If entered number is 8 and 8,
print ‘‘The numbers are equal’’. '''

# Accept input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Compare the numbers
if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
else:
    print("The numbers are equal")

