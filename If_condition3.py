"""
Program : Calculate discount for the customer with billing amount.
1. if bill amount > 1000, then discount 5% (total amount - discount/100)
2. if bill amount > 2000 and amount < 3000, then discount 10%
3. if bill amount > 3000 and amount < 4000, then discount 15%
4. if bill amount > 4000 and , then discount 25%
"""

"""
bill_amount = int(input("Please enter bill amount:"))

if bill_amount >= 1000 and bill_amount < 2000:
    discount_amount = bill_amount - bill_amount*(5/100)
    print("Please pay this amount :", discount_amount, "after 5% discount")
elif bill_amount >= 2000 and bill_amount < 3000:
    discount_amount = bill_amount - bill_amount * (10 / 100)
    print("Please pay this amount :", discount_amount, "after 10% discount")
elif bill_amount >= 3000 and bill_amount < 4000:
    discount_amount = bill_amount - bill_amount * (15 / 100)
    print("Please pay this amount :", discount_amount, "after 15% discount")
elif bill_amount >= 4000:
    discount_amount = bill_amount - bill_amount * (25 / 100)
    print("Please pay this amount :", discount_amount, "after 25% discount")
else:
    print("You have to pay full amount, there is no discount :", bill_amount)
"""

# Program : Check user is living in metro city or not.

"""
1. create metro list = ["Pune", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
2. get user city name with input method
3. Check user city name is metro list or not
"""

metro_list = ["Pune", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
user_city = input("Please enter your city name:")

"""
if user_city in metro_list:
    print("You are living metro city")
else:
    print("You are living is non metro city")

"""
#output = True if user_city in metro_list else False

output = "You are living metro city "if user_city in metro_list else "You are living is non metro city"

print("Output :", output)

"""
Program: Write a python program to create a calculator.
user_input = input("Please enter your choice\n
                    1. addition\n
                    2. multiplication\n
                    3. subtraction\n
                    4. divide\n")
                    
val1 = input("Please enter value1:")
val2 = input("Please enter value2")


"""

user_input = input("Please enter your choice\n"
                   "1. addition\n"
                   "2. multiplication\n"
                   "3. subtraction\n."
                   "4. divide\n")


