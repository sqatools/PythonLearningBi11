"""
if condition1:
    code
elif condition2
    code
elif condition3
    code
else:
    code
"""

"""
address1 = 'Pune'
address2 = 'Mumbai'
address3 = 'Bangalore'

user_input = input("Please enter your address :")

if user_input == address1:
    print("Address match, we can deliver the parcel in Pune")
elif user_input == address2:
    print("Address match, we can deliver the parcel in Mumbai")
elif user_input == address3:
    print("Address match, we can deliver the parcel in Bangalore")
else:
    print("Address did not match, we can not deliver the parcel")
    
"""

"""
db_username = 'Akshay201'
db_password = 'P@sssw0rd'

user_name = input("Please enter username:")
password = input("Please enter password:")

if user_name == db_username and password == db_password:
    print("Login Successful, Welcome:", user_name)
else:
    print("Invalid username password")
"""
"""
Nested If condition

if condition1:
    code
    if condition2:
        code
    else:
        code
else:
    code
"""

"""
num = 12

if num%3 == 0:
    print("The number is divisible by 3")
    if num%5 == 0:
        print("The number is divisible by 5 as well")
    else:
        print("The number can not divide by 5.")
else:
    print("The number can not divide by 3")

"""

round1 = "PASS"
round2 = "PASS"
round3 = "PASS"

if round1 == "PASS":
    print("Congrats your first round is clear")
    if round2 == "PASS":
        print("Congrats your second round is also cleared")
        if round3 == "PASS":
            print("Congrats you got selected, you will receive offer letter soon")
        else:
            print("Sorry, you are failed in last round")
    else:
        print("Hard luck, sorry you are failed in second round")
else:
    print("Sorry your first round is not clear, please try next time")


