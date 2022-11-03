"""
class
object
constructor
self
instance variable
inheritance
polymorphism
data hiding
"""

# Class & Object
# Class : Class is nothing but a blueprint to create a object
# Object : Through the object we can use all the properties/attribute of the class.
#          We can create millions of object of any class their is no restriction
"""
class Car:
    def car_name(self):
        print("Range Rover")

    def car_price(self):
        print("50 Lac")

    def car_brand(self):
        print("TATA")

# Create object of the class       
obj1 = Car()
obj1.car_name()

obj2 = Car()
obj2.car_brand()
"""

# Constructor : constructor which initialize the memory for the class object
# Default constructor : by default when we create object of any class then
#                      internally default constructor will be created
# Parametize constructor : when we create __init__ method with the some parameters, that knows as parametize
                       # constructor
# self : self is the object of the class in which it belongs
"""
class Car:
    def __init__(self, car_name, car_price,  car_brand):
        self.cr_name = car_name  # instance variable
        self.cr_price = car_price
        self.cr_brand = car_brand

    # instance/object method
    def car_name(self):
        print("Car name:", self.cr_name)

    def car_price(self):
        print(self.cr_price)

    def car_brand(self, param):
        print(self.cr_brand)
        print(param)


obj = Car("Baleno", "8Lac", "Maruti")

obj.car_name()

Car.car_name(obj)
#print(obj.cr_name)
#obj.car_brand()

"""

# Inheritance : when one class aquire the property of another class is known as inheritance
# 1. sinlge inheritance : A -> B
# 2. multilevel inheritance : A -> B -> C
# 3. mutiple inheritance : A -> B , C -> B
# super : super keyword we use to initialize the constructor of your super/parent class in the child class constructor

# Single Inheritance
"""
class father:
    def __init__(self,  fname, fcity,  fwealth):
        self.fname = fname
        self.fcity = fcity
        self.fwealth = fwealth

    def show_father_details(self):
        print("Father name:", self.fname)
        print("Father City:", self.fcity)
        print("Father wealth :", self.fwealth)

class child(father):
    def __init__(self, child_name, fname, fcity,  fwealth):
        super().__init__(fname, fcity,  fwealth)
        self.child_name = child_name

    def print_childname(self):
        print("child_name:", self.child_name)



fobj = father('Guptaji', 'Mumbai', '100Cr')
fobj.show_father_details()
print("_"*50)
cobj = child('Rohan', 'Guptaji', 'Mumbai', '100Cr')
cobj.show_father_details()
cobj.print_childname()
"""


# Multi level Inheritance
"""
class grandfather:
    def grand_father_method(self):
        print("My grand father is very rich person")

class father(grandfather):
    def __init__(self,  fname, fcity,  fwealth):
        self.fname = fname
        self.fcity = fcity
        self.fwealth = fwealth

    def show_father_details(self):
        print("Father name:", self.fname)
        print("Father City:", self.fcity)
        print("Father wealth :", self.fwealth)

class child(father):
    def __init__(self, child_name, fname, fcity,  fwealth):
        super().__init__(fname, fcity,  fwealth)
        self.child_name = child_name

    def print_childname(self):
        print("child_name:", self.child_name)


fobj = father('Guptaji', 'Mumbai', '100Cr')
fobj.show_father_details()
fobj.grand_father_method()
print("_"*50)
cobj = child('Rohan', 'Guptaji', 'Mumbai', '100Cr')
cobj.grand_father_method()
cobj.show_father_details()
"""

# Multiple Inheritance  # father1 -> child, father2 -> child

class A:
    def __init__(self,  Aname, Acity,  Awealth):
        self.Aname = Aname
        self.Acity = Acity
        self.Awealth = Awealth

    def show_A_details(self):
        print("Father name:", self.Aname)
        print("Father City:", self.Acity)
        print("Father wealth :", self.Awealth)


class B:
    def __init__(self, bname, bcity):
        self.bname = bname
        self.bcity = bcity

    def show_B_details(self):
        print("Father name:", self.bname)
        print("Father City:", self.bcity)

# MRO : Method resolution order
class child(B, A):
    def __init__(self, child_name, fname, fcity,  fwealth):
        super().__init__(fname, fcity,  fwealth)
        self.child_name = child_name

    def print_childname(self):
        print("child_name:", self.child_name)


obj = child('Rahul', 'Guptaji', 'Mumbai', '100Cr')

obj.show_A_details()


