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
# Inheritance : when one class aquire the property of another class, then it is known as Inheritance
# single inheritance : class A -> class B
# super() : this method helps to initiate the constructor of super/parent class into child class
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
    def __init__(self, child_name, fname, fcity, fwealth):
        super().__init__(fname, fcity, fwealth)
        self.child_name = child_name

    def print_childname(self):
        print("child_name:", self.child_name)

obj = child("Rahul", "SharmaJi", "Mumbai", "100Cr")
obj.show_father_details()
#obj.print_childname()

print("_"*30)
objp = father("GuptaJi", "Mumbai", "100Cr")
#objp.print_childname() : we won't be able to access father class.
objp.show_father_details()
"""

############### MultiLevel Inheritance ###############
"""
# A -> B -> C
class grandfather:
    def __init__(self, gfhouse):
        self.gfhouse = gfhouse

    def show_grand_father_house(self):
        print("GrandFather House:", self.gfhouse)

class father(grandfather):
    def __init__(self,  fname, fcity,  fwealth, gfhouse):
        super(father, self).__init__(gfhouse)
        self.fname = fname
        self.fcity = fcity
        self.fwealth = fwealth

    def show_father_details(self):
        print("Father name:", self.fname)
        print("Father City:", self.fcity)
        print("Father wealth :", self.fwealth)
        print("Father Gf and House", self.gfhouse)

class child(father):
    def __init__(self, child_name, fname, fcity, fwealth, gfhouse):
        super().__init__(fname, fcity, fwealth, gfhouse)
        self.child_name = child_name

    def print_childname_its_house(self):
        print("child_name:", self.child_name)
        print("child and grandfather house ")
        self.show_grand_father_house()


obj = child("Mehul", "VermaJi", "Bangalore", "150Cr", "Banglow")
obj.show_father_details()
obj.print_childname_its_house()
"""

########################## Multi Level Inheritance ###############

class A:
    def __init__(self, vara):
        self.vara = vara

    def class_a_method(self):
        print("this is class A data:", self.vara)


class B:
    def __init__(self, varb1, varb2):
        self.varb1 = varb1
        self.varb2 = varb2

    def class_b_method(self):
        print("this is class B data:",  self.varb1, self.varb2)

# MRO : Method resolution order :
# The order calling classes will depend constructor initialization which one will get priority

class C(B, A):
    def __init__(self, varc, varb1, varb2, vara):
        self.varc = varc
        self.vara = vara
        super(C, self).__init__(varb1, varb2)

    def initiate_classa(self):
        return A(self.vara)

    def class_c_method(self):
        print("this is class A")


objc = C('100', '50', '51', 60)
objc.class_b_method()
obja = objc.initiate_classa()
obja.class_a_method()

# Interview Question
"""
-> What is inheritance and its Type
Inheritance : when one class aquire the property of another class, then it is known as Inheritance

Type : Single Inheritance : A -> B
     : Multi Level Inheritance : A -> B -> C
     : Multiple Inheritance : A -> B, C -> B

-> Different between multi level and multiple inheritance 

multi level : A -> B -> C

multiple -> A -> B, C -> B

-> What is MRO (Method Resolution Order) : which constructor will get priority to initiate the constructor, its
depends on orders of calling the classes as part of inheritance.

-> What is Super() : This keyword help to initiate the constructor of super into child class.
"""
