# Write a program that accepts an input from a user. Print ‘Even number’ if entered value is 
# even or print ‘Odd number’ if entered value is odd. You must make sure the entered value 
# is a number. If the entered value is not a number, print ‘Enter a valid number’.


# Accept input from the user
user_input = input("Enter a number: ")

# Check if the input is a valid number
if user_input.isdigit():
    number = int(user_input)
    # Check if the number is even or odd
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Enter a valid number")

