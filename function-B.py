''' Write a program that accepts input from user. Print True if entered value is divisible by 5, 
otherwise print False. '''

# Accept input from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 5
if number % 5 == 0:
    print(True)
else:
    print(False)
