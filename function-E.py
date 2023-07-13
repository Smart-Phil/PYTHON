'''
Coca Cola recently announced a discount of 10% if a customer buys Coke worth more than 
1000 Naira. If one coke costs 200 Naira. Write a program that allows the customer enter 
the quantity of coke he/she wants to buy. Then calculate and print the amount the customer 
is expected to pay. E.g if a customer wants to buy 7 cokes, print ‘1260 Naira’. '''



# Constants
COST_PER_COKE = 200
DISCOUNT_THRESHOLD = 1000
DISCOUNT_PERCENTAGE = 0.1

# Accept input from the user
quantity = int(input("Enter the quantity of Coke you want to buy: "))

# Calculate the total cost
total_cost = quantity * COST_PER_COKE

# Apply discount if applicable
if total_cost > DISCOUNT_THRESHOLD:
    discount = total_cost * DISCOUNT_PERCENTAGE
    total_cost -= discount

# Print the amount the customer is expected to pay
print(f"{total_cost} Naira")

