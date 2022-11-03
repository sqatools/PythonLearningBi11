"""
def show_name(func):
    def inner():
        print(f"Hello Mr:", 'Vaibhav')
        func()
    return inner

@show_name
def greeting():
    print("Good Morning")

greeting()
"""


def show_name(*args, **kwargs):
    def inner(func):
        #print(f"My name is:{kwargs['name']}")
        print(f"{kwargs['msg']}")
        func(kwargs['word'])
    return inner

# @show_name(msg='We are learning Python', name='Yogesh')
# def greeting():
#     print("Good Morning")

print("_"*40)

@show_name(msg='It will show repeated word', word='Python')
def print_repeated_word(word):
    print(word*5)


# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))


print(factorial(5))
# n= 5, fact 5*factorial(5-1)
# n =4, fact 5*4*factorial(4-1)
# n = 3, fact 5*4*3*factorial(3-1)
# n = 2, fact 5*4*3*2factorial(2-1)
# n = 1  fact 5*4*3*2*1
