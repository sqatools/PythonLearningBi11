# num1 = 10
# print(num1/0)
"""
try:
    code
except:
    print()
"""
"""
try:
    num1 = 10
    num2 = 2
    print(num1/num2)
except:
    print("Divide by zero is not allowed")
"""

# Catch exception with var and provide system generated error as well customized msg
"""
try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except Exception as e:
    print("Divide by zero is not allowed")
    print(e)
"""


# raise the catched exception that will fail the program
"""
try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except Exception as e:
    print("Divide by zero is not allowed")
    raise e
"""

#AttributeError
"""
try:
    str1 = "Good Morning"
    str1.replace("Good")
except Exception as e:
    raise e   # TypeError: replace expected at least 2 arguments, got 1
"""

def addition(num1, num2):
    print(num1+num2)

"""
def check_execution():
    try:
        addition(30,'Hello')
        return True
    except Exception as e:
        raise
        #return False, e

output = check_execution()
print(output)
"""

# Exception with else : else condition will execute when there is no exeception in the program.
"""
try:
    addition(40, "50")
    print("Execution successful")
except Exception as e:
    print(e)
    print("Execution un-successful")
else:
    print("Multiplication:", 50*6)
   
"""

# finally : finally code will execution even there is exeception in the code or not.
"""
list1 = [5, 7, 8, 2, 11]
try:
    addition(40, "Hello")
    print("Execution successful")
except Exception as e:
    print(e)
    print("Execution un-successful")
finally:
    for val in list1:
        if val%2 != 0:
            print(val)
        else:
            continue

"""
# Exception with else and finally block.
"""

list1 = [5, 7, 8, 2, 11]
try:
    addition(40, "Python")
    print("Execution successful")
except Exception as e:
    print(e)
    print("Execution un-successful")
else:
    # this block will not execute if there is any exception in the code
    print("Multiplication:", 50*3)
finally:
    # This block will execute even there is exception in the code or not exception.
    for val in list1:
        if val%2 != 0:
            print(val)
        else:
            continue
"""
# 1. try and except
# 2. there is way to raise exception using "raise".
# 3. exception with else, this will execute only there is no exception
# 4 exception with finally , finally code will execute in all the conditions.


try:
    print("addition :", 20+ 30)
    try:
        print("multiplication:", 50/0)
    except Exception as e:
        print("Multiplication Error:", e)
        raise

    print("Repeat char:", "Python"*5)


except Exception as e:
    print("Addition Error:", e)


