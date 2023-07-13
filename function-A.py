''' Write a program that allows a user to enter his/her age to check his/her eligibility to vote. 
Print ‘Eligible, kindly cast your vote’ if entered age is greater than 18, otherwise print 
‘Ineligible, please come back when you are 18’. '''

age = int(input("Enter your age: "))

if age > 18:
	print("Eligible, kindly cast your vote.")
else:
	print("Ineligible, please come back when you are 18.")

