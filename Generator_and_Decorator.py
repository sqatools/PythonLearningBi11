# Generator

"""
def show_msg():
    return "Hello Good Morning"
    #return "Hello Good Morning"

output = show_msg()
print(output)
"""


def show_msgs():
    yield "We are learning Python"
    yield "How are you ?"
    yield "Good morning"

output1 = show_msgs()
print(output1)
"""
print(next(output1))
print(next(output1))
print(next(output1))
print(next(output1))
#"""
list1 = [5, 7, 8 ,2, 4]

output2 = reversed(list1)
print(output2)
print(next(output2))
print(next(output2))


def get_square_of_number():
    list1 = [5, 7, 3, 8, 9]
    output = [x**2 for x in list1]
    return output

output3 = get_square_of_number()
print(output3)


def get_square_of_number1():
    list1 = [5, 7, 3, 8, 9]
    for x in list1:
        yield x**2

result = get_square_of_number1()
print(result)
print(next(result))
