"""
str1 = "Hello"
output = str1.lower()
print(output)
"""
str1 = "Hello"
output = str1.lower()
"""

def function1(num1, num2):
    print(num1+num2)

output = function1(50, 30)
print(output)

def function2(num1, num2):
    return num1+num2

output1 = function2(60, 40)
print("output1 :", output1*3)


def function3(num1, num2):
    x = num1 + num2
    y = num1 * num2
    return x, y

output3 = function3(40, 30)
print("output3 :", output3)

p ,q =  function3(60, 3)

print("p :", p,"q:", q)

def get_square(list1):
    output = [x**2 for x in list1]
    return output

def get_division_of_square(list1):
    output = get_square(list1)
    print("output :", output)
    result = [x//2 for x in output]
    return result

var = get_division_of_square([5, 7, 2, 4, 8])
print(var)
"""
"""
Variables scope

Global Variable : If we defined any variable outside of the function then the scope of the
         variable is global scope, it means any function which belongs that module can
         easily access.
         
Local Variable : The variable we defined inside the function is known as local variable,
        scope of the variable will limited to that function only.
          
Nonlocal : Non local variable is global variable for nested functions and scope is limited 
         outer function only
"""
"""
# Global variable
varx = 10

def new_function1():
    vary = 50 # local variable
    varx = 70 # Local variable
    print("varx :", varx)
    print("vary :", vary)

def new_function2():
    varz = 60 # local variable
    print("varx :", varx)
    #print("vary :", vary) # can not access local variable of any other function
    print("varz :", varz)


new_function1()
print("_"*40)
new_function2()
"""

###################################

"""
# Global variable
varx = 10

def new_function1():
    global varx
    vary = 50 # local variable
    varx = 100
    print("varx :", varx)
    print("vary :", vary)

def new_function2():
    varz = 60 # local variable
    print("varx :", varx)
    #print("vary :", vary) # can not access local variable of any other function
    print("varz :", varz)

def new_function3():
    varp = 80 # local variable
    print("varx :", varx)
    #print("vary :", vary) # can not access local variable of any other function
    print("varp :", varp)

varx = 90
new_function3()
print("_"*40)
new_function1()
print("_"*40)
new_function2()
"""

############ non local ###########
vara = 30 # global var

def outer_func():
    varb = 50 # non local variable

    def inner_func1():
        print("---inner function1---")
        global vara
        nonlocal varb
        varc = 40 # local variable
        vara = 70 # local variable
        varb = 80 # local variable
        print("vara:", vara)
        print("varb:", varb)
        print("varc:", varc)

    def inner_func2():
        print("---inner function2---")
        vard = 40 # local variable
        print("vara:", vara)
        print("varb:", varb)
        print("vard:", vard)
        # print("varc:", varc) # can not access local variable of any other function

    inner_func1()
    inner_func2()

outer_func()


"""
-> simple function definition
-> function  with parameter : pass bye value, pass by refrence
-> function with default parameter values.
-> function with list of values *args
-> function with key value pair as input
-> call function in other module/files.
-> get return value from the function
-> call function inside the other function
-> check local, global and non local variable scope.
"""

def learning(num1: int, str1: str, list1: list, tuple1 : tuple) -> tuple:
    """ This function will perform multiple operation with int, str, list and tuples
    values as input
    :param int num1: this number will perform some mathc operation
    :param str str1: this string will manupulate and return output
    :param list list1: this list will provide square all the values in the list
    :param tuple tuple1: we will fixed values as part of tuple
    :return: tuple
    """
    return num1, str1, list1, tuple1

print(learning.__doc__)  # we can read documentations of given function

print(learning(345, 'Hello', [5, 7, 8], (7, 8, 2) ))



