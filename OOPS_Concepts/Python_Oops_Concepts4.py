"""
class
object
methods
constructor
self
instance variable
inheritance
polymorphism
data hiding
static method
class method

"""
# Polymorphism : multiple task perform by single element.
# Method Overriding : when parent and child class have same method name, but their content is different
# this concept is known method overriding.

# Method Overloading : When one class has two method with same name with different parameters then
# this concept is known as method over loading : But python does not support.

"""
class A:
    def __init__(self, vara):
        self.vara = vara

    def class_a_method(self):
        print("this is class A data:", self.vara)

    def show_class_data(self):
        print("class data A:", self.vara)

class B(A):
    def __init__(self, varb1, varb2,  vara):
        super().__init__(vara)
        self.varb1 = varb1
        self.varb2 = varb2

    def class_b_method(self):
        print("this is class B data:", self.varb1)

    def show_class_data(self):
        print("class data B:", self.varb1, self.varb2)


obj = B(50, 60, 70)
obj.show_class_data()

"""

# Method Overloading
""""
class A:
    def __init__(self, vara):
        self.vara = vara

    def class_method_a(self, list):
        for var in list:
            print(var, end=" ")

    def class_method_a(self, num1, num2):
        print("addition  :", num1 + num2)

    def show_class_data(self):
        print("class data A:", self.vara)

obj = A(50)
#obj.class_method_a([4, 7, 8]) # it wont work because python use latest defined method only.
obj.class_method_a(6, 8)

"""

# Operator Overloading : One Operator which perform multiple task like Plus operator and multiplication
# Operator
"""
num1 = 40
num2 = 50

print("output : ", num1 + num2)
print("output :", num1.__add__(num2))

str1 = "Hello"
str2 = "Good Morning"

print("str output :", str1 + str2)
print("str output :", str1.__add__(str2))

num1 = 70
num2 = 70

print(num1 == num2)
print(num1.__eq__(num2))
print(num1.__mul__(num2))
"""


################# Data Hiding ##########
"""
single under score "_"
double under score   "__"
"""

"""
-> We we defined any variable/method with single/double underscore as prefix then those data 
will not show in suggestion list

-> If we want access any single underscore prefix variable/method, then we can access them directly 
with the name.

-> If we want to any any double underscore variable/method, then we have to use special sysntax
obj._<clasname>.__variable/method()

"""

class school:
    # class variable
    name = "Convent School"
    _city = "Mumbai"
    __address  = "Borvali"

    def __init__(self,  fee, standard,  groud):
        self.fee = fee
        self._stand = standard
        self.__ground = groud

    def show_school_fee(self):
        print("standard:",  self._stand)

    def _check_groud_availability(self):
        print("Availability :", self.__ground)

    def __show_all_details(self):
        print("fee :", self.fee)
        print("standard :", self._stand)
        print("ground :", self.__ground)

    @classmethod
    def show_school_city(cls):
        print(cls._city)

    @classmethod
    def school_class_method(cls):
        print(cls.name)
        cls.show_school_city()

    @staticmethod
    def multiplication_number(num1, num2):
        print(num1*num2)


#obj = school("2lAc", "1oth", "Yes")

#print(obj.name)


# obj._check_groud_availability()

# way to access double underscore method or variable obj._classname__variable

# print(obj._school__address)

#obj.school_class_method()

school.multiplication_number(4, 5)


