"""
def myTechFocus():
    code
"""

def myTechFocus():
    print("We are My Tech Focus students")
#myTechFocus()
#myTechFocus()

# function with parameters
def myTechFocusTraining(name):
    print(f"My name is {name}, and I am learning Python")







"""
# Pass by value
myTechFocusTraining('Tushar')

# pass by reference
st_name = 'Yogesh'
myTechFocusTraining(st_name)

myTechFocusTraining(name='Keshav')

myTechFocusTraining(('Anand', 'raj', 'Pradip'))
myTechFocusTraining(['An', 'ra', 'Pr'])
"""


def addition(num1, num2):
    print("Num1:", num1)
    print("Num2:", num2)
    print("addition :", num1+ num2)

#addition(10, 20)
#addition(num2=10, num1=20)
#st_name = 'Yogesh'

#Function with default parameter value
# the parameter which has default should always on right side

def fucntion2(num1, num2=60):
    print("num1:", num1)
    print("num2:", num2)
    print("multiplication :", num1*num2)
"""
fucntion2(100)
fucntion2(100, 7)
fucntion2(num2=6)  # fucntion2() missing 1 required positional argument: 'num1'
"""

# *args

def function4(*abhi):
    print(abhi)
    for val in abhi:
        print(val)

#function4(8, 2, 4, 2, 6, 'Python', (5, 7, 8), [2, 4, 6])
"""
# Program1 : write a python function to get all the prime from given list

list1 = [11, 44, 23, 61, 29, 8, 12, 15]
output = [11, 23, 29]

# Program2 : write python function to check the given list values sum is available in target list

list1 = [5, 7, 2, 8, 8]
list2 = [1, 6, 8, 2, 9]
sum_list = [6, 13, 11, 10, 18]

Output = [(11,2),  (18, 4)]

# Program3 : Write a python function to check given number belongs to which key of the dictionary
dict1 = {'a' : 68, 'b': 23, 'c': 34}
num1 = 23

output = {'b': 23}
"""

# **kwargs : to get function parameters in key value format

def function5(**kwargs):
    print(kwargs)

function5(name='Abhi', age=23, email='abhi@gmail.com')

def login(**kwargs):
    db_username = 'sagar123'
    db_password = "admin@123"
    print(kwargs['email'])
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Invalid username password")

login(username='sagar1234', password='admin@123', email='sagar@gmail.com')